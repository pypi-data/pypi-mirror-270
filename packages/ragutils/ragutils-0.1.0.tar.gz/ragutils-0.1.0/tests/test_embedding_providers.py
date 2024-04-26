import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ragutils.embedding_providers import EmbeddingProvider

class TestEmbeddingProvider:
    @pytest.fixture
    def openai_embedding_provider(self):
        return EmbeddingProvider(embedding_provider="openai")

    def test_get_embedding_function_openai(self, openai_embedding_provider):
        embedding_function = openai_embedding_provider.get_embedding_function(model_name="text-embedding-3-small")
        assert embedding_function is not None  

    @pytest.fixture
    def google_embedding_provider(self):
        return EmbeddingProvider(embedding_provider="google")

    def test_get_embedding_function_google(self, google_embedding_provider):
        embedding_function = google_embedding_provider.get_embedding_function()
        assert embedding_function is not None 

    @pytest.fixture
    def cohere_embedding_provider(self):
        return EmbeddingProvider(embedding_provider="cohere")

    def test_get_embedding_function_cohere(self, cohere_embedding_provider):
        embedding_function = cohere_embedding_provider.get_embedding_function()
        assert embedding_function is not None 

    @pytest.fixture
    def huggingface_embedding_provider(self):
        return EmbeddingProvider(embedding_provider="huggingface")

    def test_get_embedding_function_huggingface(self, huggingface_embedding_provider):
        embedding_function = huggingface_embedding_provider.get_embedding_function(model_name = "BAAI/bge-base-en-v1.5")
        assert embedding_function is not None 

    @pytest.fixture
    def qdrant_embedding_provider(self):
        return EmbeddingProvider(embedding_provider="qdrant")

    def test_get_embedding_function_qdrant(self, qdrant_embedding_provider):
        embedding_function = qdrant_embedding_provider.get_embedding_function()
        assert embedding_function is not None 


