import os
from pinecone import Pinecone, ServerlessSpec
from typing import Optional, List
from langchain.docstore.document import Document
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS, Chroma, Milvus, Qdrant, DocArrayInMemorySearch
from settings import Settings

class VectorDatabase:
    def __init__(self, vector_store, index_name):
        """
        A class for managing vector databases.

        Args:
            vector_store (str): The name of the vector store to use.
            index_name (str): The name of the index to use.
        """
        self.vector_store = vector_store
        self.index_name = index_name

    def create_index(self, embedding_function: str, docs: List[Document], index_dir: Optional[str] = None, **kwargs):
        """
        Creates an index for the given documents using the specified embedding function.

        Args:
            embedding_function (str): The name of the embedding function to use.
            docs (List[Document]): The list of documents to index.
            index_dir (Optional[str]): The directory to store the index in. If not specified, the index will be stored in memory.
            **kwargs: Additional arguments specific to the vector store being used.

        Returns:
            The index object.
        """
        if index_dir:
            if os.path.exists(index_dir):
                persist_directory = os.path.join(index_dir, self.index_name)
            else:
                os.makedirs(index_dir)
                persist_directory = os.path.join(index_dir, self.index_name)
        else:
            persist_directory = self.index_name

        if self.vector_store == 'chroma':
            vector_index = Chroma.from_documents(docs, embedding_function, persist_directory=persist_directory)
            return vector_index.persist()

        elif self.vector_store == 'pinecone':
            pc = Pinecone(api_key=Settings.get_pinecone_api_key())
            dimension = kwargs.get('dimension', 768)
            metric = kwargs.get('metric', 'cosine')
            spec = kwargs.get('spec', ServerlessSpec(cloud="aws", region="us-east-1"))
            if self.index_name not in pc.list_indexes():
                pc.create_index(self.index_name, dimension=dimension, metric=metric, spec=spec)

            vector_index = PineconeVectorStore.from_documents(docs, embedding_function, index_name=self.index_name)
            return vector_index

        elif self.vector_store == 'milvus':
            vector_index = Milvus.from_documents(docs, embedding_function, collection_name=self.index_name,
                                                  connection_args={'host': Settings.get_milvus_host(),
                                                                   'port': Settings.get_milvus_port()})

            return vector_index

        elif self.vector_store == 'qdrant':
            qdrant_environment = Settings.get_qdrant_environment()
            if qdrant_environment == 'memory':
                vector_index = Qdrant.from_documents(docs, embedding_function, collection_name=self.index_name,
                                                      location=":memory:")
            elif qdrant_environment == 'disk':
                vector_index = Qdrant.from_documents(docs, embedding_function, collection_name=self.index_name,
                                                      path=index_dir)
            elif qdrant_environment == 'on_premise':
                vector_index = Qdrant.from_documents(docs, embedding_function, collection_name=self.index_name,
                                                      prefer_grpc=True, url=Settings.get_qdrant_url())
            elif qdrant_environment == 'cloud':
                vector_index = Qdrant.from_documents(docs, embedding_function, collection_name=self.index_name,
                                                      prefer_grpc=True, url=Settings.get_qdrant_url(),
                                                      api_key=Settings.get_qdrant_api_key())
            else:
                raise ValueError(
                    'Invalid environment value: Expecting one of memory, disk, on_premise or cloud')

        elif self.vector_store == 'array':
            vector_index = DocArrayInMemorySearch.from_documents(docs, embedding_function, index_name=persist_directory)
            return vector_index

        elif self.vector_store == 'faiss':
            vector_index = FAISS.from_documents(docs, embedding_function)
            return vector_index.save_local(persist_directory)

        else:
            raise ValueError(
                'Invalid vector_store value: Expecting one of chroma, pinecone, milvus, qdrant, faiss or array')
