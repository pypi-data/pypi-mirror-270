from typing import Optional
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import FastEmbedEmbeddings, HuggingFaceInferenceAPIEmbeddings, OllamaEmbeddings
from langchain_cohere import CohereEmbeddings
from settings import Settings

class EmbeddingProvider:
    """
    A class that provides different embedding functions based on the embedding_provider specified in the settings file.
    """
    def __init__(self, embedding_provider: str):
        """
        Initialize the EmbeddingProvider class.

        Args:
            embedding_provider (str): The name of the embedding provider.
        """
        self.embedding_provider = embedding_provider

    def get_embedding_function(self, model_name: Optional[str] = None):
        """
        Get the embedding function based on the embedding_provider and model_name.

        Args:
            model_name (str, optional): The name of the model. Defaults to None.

        Returns:
            The embedding function.
        """
        if self.embedding_provider == "openai":
            openai_api_key = Settings.get_openai_api_key()
            if model_name:
                return OpenAIEmbeddings(model=model_name, openai_api_key=openai_api_key)
            else:
                return OpenAIEmbeddings(openai_api_key=openai_api_key)
        elif self.embedding_provider == "cohere":
            cohere_api_key = Settings.get_cohere_api_key()
            if model_name:
                return CohereEmbeddings(model_name, cohere_api_key=cohere_api_key)
            else:
                return CohereEmbeddings(cohere_api_key=cohere_api_key)
        elif self.embedding_provider == "huggingface":
            huggingface_api_key = Settings.get_huggingface_api_key()
            # INFERENCE api does not download the models locally so it is fast
            return HuggingFaceInferenceAPIEmbeddings(model_name=model_name or "sentence-transformers/all-MiniLM-l6-v2", api_key=huggingface_api_key)

        elif self.embedding_provider == "ollama":
            if model_name:
                return OllamaEmbeddings(model_name)
            else:
                return OllamaEmbeddings()
        elif self.embedding_provider == "google":
            google_api_key = Settings.get_google_api_key()
            return GoogleGenerativeAIEmbeddings(model=model_name or "models/embedding-001", google_api_key=google_api_key)

        elif self.embedding_provider == 'qdrant':
            # Assuming FastEmbedEmbeddings doesn't require any API key
            if model_name:
                return FastEmbedEmbeddings(model_name)
            else:
                return FastEmbedEmbeddings()

        else:
            raise ValueError(
                f"Embedding provider {self.embedding_provider} is not supported. We currently support openai, google, cohere, huggingface, qdrant and ollama as embedding providers")
