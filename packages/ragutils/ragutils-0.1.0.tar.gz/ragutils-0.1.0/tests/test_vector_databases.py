import os
import sys
import pytest
from pinecone import ServerlessSpec
from dotenv import load_dotenv
# from langchain_community.vectorstores import Milvus
from langchain_pinecone import PineconeVectorStore
from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ragutils.document_loaders import DocumentLoader
from src.ragutils.embedding_providers import EmbeddingProvider
from src.ragutils.text_splitters import TextSplitter
from src.ragutils.vector_databases import VectorDatabase  
from settings import Settings  

class TestVectorDatabase:
    load_dotenv()
    document_loader = DocumentLoader()
    text_splitter = TextSplitter(splitter='recursive')
    embedding_provider = EmbeddingProvider('huggingface')
    
    @pytest.fixture
    def chroma_vector_database(self):
        return VectorDatabase(vector_store='chroma', index_name='test_chroma')
    
    def test_create_index_chroma(self, chroma_vector_database):
        index_dir='tests/index/'
        file_path = "tests/test_data/attention.pdf"
        embedding_function =  self.embedding_provider.get_embedding_function()
        data = self.document_loader.load_and_get_data(file_path=file_path)
        docs = self.text_splitter.split_to_documents(data)
        chroma_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir)
        assert os.path.exists(os.path.join(index_dir, "test_chroma"))

    @pytest.fixture
    def faiss_vector_database(self):
        return VectorDatabase(vector_store='faiss', index_name='test_faiss')
    
    def test_create_index_faiss(self, faiss_vector_database):
        index_dir='tests/index/'
        file_path = "tests/test_data/attention.pdf"
        embedding_function =  self.embedding_provider.get_embedding_function()
        data = self.document_loader.load_and_get_data(file_path=file_path)
        docs = self.text_splitter.split_to_documents(data)
        faiss_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir)
        assert "test_faiss" in os.listdir(index_dir)
        assert os.path.exists(os.path.join(index_dir, "test_faiss"))

    @pytest.fixture
    def qdrant_vector_database(self):
        return VectorDatabase(vector_store='qdrant', index_name='test_qdrant')
    
    def test_create_index_qdrant(self, qdrant_vector_database):
        index_dir='tests/index/'
        file_path = "tests/test_data/attention.pdf"
        embedding_function =  self.embedding_provider.get_embedding_function()
        data = self.document_loader.load_and_get_data(file_path=file_path)
        docs = self.text_splitter.split_to_documents(data)
        qdrant_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir)
        assert os.path.exists(os.path.join(index_dir, "collection", "test_qdrant"))

    # #this milvus test should be done locally with a linux system or wsl in windows
    # @pytest.fixture
    # def milvus_vector_database(self):
    #     return VectorDatabase(vector_store='milvus', index_name='test_milvus')
    
    # def test_create_index_milvus(self, milvus_vector_database):
    #     index_dir='tests/index/'
    #     file_path = "tests/test_data/attention.pdf"
    #     embedding_function =  self.embedding_provider.get_embedding_function()
    #     data = self.document_loader.load_and_get_data(file_path=file_path)
    #     docs = self.text_splitter.split_to_documents(data)
    #     milvus_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir)
        
    #     assert Milvus(embedding_function, connection_args = {"host": Settings.get_milvus_host(), "port": Settings.get_milvus_port() }, collection_name="test_milvus") is not None

    @pytest.fixture
    def pinecone_vector_database(self):
        return VectorDatabase(vector_store='pinecone', index_name='test-pinecone')
    
    def test_create_index_pinecone(self, pinecone_vector_database):
        index_dir='tests/index/'
        file_path = "tests/test_data/attention.pdf"
        embedding_function =  self.embedding_provider.get_embedding_function()
        data = self.document_loader.load_and_get_data(file_path=file_path)
        docs = self.text_splitter.split_to_documents(data)
        pinecone_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir, dimension=384, metric="cosine", spec = ServerlessSpec(cloud="aws", region="us-east-1") )
        
        assert PineconeVectorStore(index_name="test-pinecone", embedding=embedding_function)
    @pytest.fixture
    def qdrant_cloud_vector_database(self):
        return VectorDatabase(vector_store='qdrant', index_name='test_qdrant_cloud')
    
    def test_create_index_qdrant_cloud(self, qdrant_cloud_vector_database):
        """https://pypi.org/project/qdrant-client/"""
        index_dir='tests/index/'
        file_path = "tests/test_data/attention.pdf"
        embedding_function =  self.embedding_provider.get_embedding_function()
        data = self.document_loader.load_and_get_data(file_path=file_path)
        docs = self.text_splitter.split_to_documents(data)
        qdrant_cloud_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir)
        client = QdrantClient(url = Settings.get_qdrant_url(), api_key = Settings.get_qdrant_api_key())
        assert Qdrant(client = client, collection_name = "test_qdrant_cloud", embeddings=embedding_function) is not None

    @pytest.fixture
    def array_vector_database(self):
        return VectorDatabase(vector_store='array', index_name='test_array')
    
    def test_create_index_array(self, array_vector_database):
        index_dir='tests/index/'
        file_path = "tests/test_data/attention.pdf"
        embedding_function =  self.embedding_provider.get_embedding_function()
        data = self.document_loader.load_and_get_data(file_path=file_path)
        docs = self.text_splitter.split_to_documents(data)
        assert array_vector_database.create_index(embedding_function=embedding_function, docs=docs, index_dir=index_dir) is not None