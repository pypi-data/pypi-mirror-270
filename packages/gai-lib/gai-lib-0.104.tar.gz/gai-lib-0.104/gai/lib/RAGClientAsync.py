import asyncio
import os
import json
import uuid
from gai.common.http_utils import http_post_async, http_get_async,http_delete_async, http_put_async
from gai.common.logging import getLogger
from gai.common.errors import ApiException
logger = getLogger(__name__)
logger.setLevel("DEBUG")
from gai.lib.ClientBase import ClientBase
import websockets
from gai.common.StatusListener import StatusListener

class RAGClientBase(ClientBase):
    
    def __init__(self,config_path=None):
        super().__init__(config_path)
        self.base_url = os.path.join(
            self.config["gai_url"], 
            self.config["generators"]["rag"]["url"].lstrip('/'))
        logger.debug(f'base_url={self.base_url}')

    def _prepare_files_and_metadata(self, collection_name, file_path, metadata):
        mode = 'rb' if file_path.endswith('.pdf') else 'r'
        with open(file_path, mode) as f:
            files = {
                "file": (os.path.basename(file_path), f if mode == 'rb' else f.read(), "application/pdf"),
                "metadata": (None, json.dumps(metadata), "application/json"),
                "collection_name": (None, collection_name, "text/plain")
            }
            return files

class RAGClientAsync(RAGClientBase):

    def __init__(self,config_path=None):
        super().__init__(config_path)

    ### ----------------- MULTI-STEP INDEXING ----------------- ###
    async def index_document_header_async(
        self, 
        collection_name, 
        file_path, 
        file_type="",
        title="",
        source="",
        authors="",
        publisher="",
        published_date="",
        comments="",
        keywords=""):
        
        url=os.path.join(self.base_url,"step/header")
        metadata = {
            "title": title,
            "file_type":file_type,
            "source": source,
            "authors": authors,
            "publisher": publisher,
            "published_date": published_date,
            "comments": comments,
            "keywords": keywords
        }

        # Send file
        try:
            mode = 'rb'
            with open(file_path, mode) as f:
                files = {
                    "file": (os.path.basename(file_path), f, "application/pdf"),
                    "metadata": (None, json.dumps(metadata), "application/json"),
                    "collection_name": (None, collection_name, "text/plain")
                }

                response = await http_post_async(url=url, files=files)
                if not response:
                    raise Exception("No response received")

                return response.json()
        except Exception as e:
            logger.error(f"index_document_header_async: Error creating document header. error={e}")
            raise e


    async def index_document_split_async(
            self,
            collection_name,
            document_id,
            chunk_size,
            chunk_overlap):
        url=os.path.join(self.base_url,"step/split")
        try:
            response = await http_post_async(url=url, data={
                "collection_name": collection_name,
                "document_id": document_id,
                "chunk_size": chunk_size,
                "chunk_overlap": chunk_overlap
            })
            return response.json()
        except Exception as e:
            logger.error(f"index_document_split_async: Error splitting document. error={e}")
            raise e

    async def index_document_index_async(
            self,
            collection_name,
            document_id,
            chunkgroup_id,
            listener_callback=None):
        url=os.path.join(self.base_url,"step/index")
        try:
            # Spin off listener task if listener_callback is provided
            listen_task=None
            if listener_callback:
                ws_url=os.path.join(self.base_url,f"index-file/ws").replace("http","ws")
                listener = StatusListener(ws_url, collection_name)
                listen_task=asyncio.create_task(listener.listen(listener_callback))

            response = await http_post_async(url=url, data={
                "collection_name": collection_name,
                "document_id": document_id,
                "chunkgroup_id":chunkgroup_id
            })

            # Cancel listener task if it was started
            if listen_task:
                listen_task.cancel()

            return response.json()
        except Exception as e:
            logger.error(f"index_document_split_async: Error splitting document. error={e}")
            raise e


    ### ----------------- SINGLE-STEP INDEXING ----------------- ###
    async def index_document_async(
        self, 
        collection_name, 
        file_path,
        file_type="", 
        title="",
        source="",
        authors="",
        publisher="",
        published_date="",
        comments="",
        keywords="", 
        listener_callback=None):
        
        url=os.path.join(self.base_url,"index-file")
        metadata = {
            "title": title,
            "source": source,
            "file_type": file_type,
            "authors": authors,
            "publisher": publisher,
            "published_date": published_date,
            "comments": comments,
            "keywords": keywords
        }

        # Send file
        try:
            mode = 'rb'
            with open(file_path, mode) as f:
                files = {
                    "file": (os.path.basename(file_path), f, "application/pdf"),
                    "metadata": (None, json.dumps(metadata), "application/json"),
                    "collection_name": (None, collection_name, "text/plain")
                }
        
                # Spin off listener task if listener_callback is provided
                listen_task=None
                if listener_callback:
                    ws_url=os.path.join(self.base_url,f"index-file/ws").replace("http","ws")
                    listener = StatusListener(ws_url, collection_name)
                    listen_task=asyncio.create_task(listener.listen(listener_callback))

                response = await http_post_async(url=url, files=files)
                if not response:
                    raise Exception("No response received")

                # Cancel listener task if it was started
                if listen_task:
                    listen_task.cancel()

                return response.json()
        except Exception as e:
            logger.error(f"index_document_async: Error indexing file. error={e}")
            raise e
    
    ### ----------------- RETRIEVAL ----------------- ###

    async def retrieve_async(self, collection_name, query_texts, n_results=None):
        url = os.path.join(self.base_url,"retrieve")
        data = {
            "collection_name": collection_name,
            "query_texts": query_texts
        }
        if n_results:
            data["n_results"] = n_results

        response = await http_post_async(url, data=data)
        return response.json()["retrieved"]

#Collections-------------------------------------------------------------------------------------------------------------------------------------------

    async def delete_collection_async(self, collection_name):
        url = os.path.join(self.base_url,"collection",collection_name)
        logger.info(f"RAGClient.delete_collection: Deleting collection {url}")
        try:
            response = await http_delete_async(url)
        except ApiException as e:
            if e.code == 'collection_not_found':
                return {"count":0}
            logger.error(e)
            raise e
        return json.loads(response.text)

    async def list_collections_async(self):
        url = os.path.join(self.base_url,"collections")
        response = await http_get_async(url)
        return json.loads(response.text)

#Documents-------------------------------------------------------------------------------------------------------------------------------------------

    async def list_documents_async(self):
        url = os.path.join(self.base_url,"documents")
        response = await http_get_async(url)
        return json.loads(response.text)
    
    async def list_documents_by_collection_async(self,collection_name):
        url = os.path.join(self.base_url,f"collection/{collection_name}/documents")
        response = await http_get_async(url)
        return json.loads(response.text)

#Document-------------------------------------------------------------------------------------------------------------------------------------------

    async def get_document_async(self, collection_name, document_id):
        url = os.path.join(self.base_url,f"collection/{collection_name}/document/{document_id}")
        response = await http_get_async(url)
        return json.loads(response.text)


    async def delete_document_async(self,collection_name,document_id):
        url = os.path.join(self.base_url,f"collection/{collection_name}/document/{document_id}")
        response = await http_delete_async(url)
        return json.loads(response.text)
    
    async def update_document_async(self,collection_name,document_id,metadata):
        url = os.path.join(self.base_url,f"collection/{collection_name}/document/{document_id}")
        response = await http_put_async(url,data=metadata)
        return json.loads(response.text)

#Chunks-------------------------------------------------------------------------------------------------------------------------------------------

    async def list_document_chunks_async(self,collection_name,document_id):
        url = os.path.join(self.base_url,f"collection/{collection_name}/document/{document_id}/chunks")
        response = await http_get_async(url)
        return json.loads(response.text)
    
    async def get_chunk_async(self,collection_name,chunk_id):
        url = os.path.join(self.base_url,f"collection/{collection_name}/chunk/{chunk_id}")
        response = await http_get_async(url)
        return json.loads(response.text)