# **ragutils**
* A Python package that abstracts RAG (Retrieval-Augmented Generation) utilities, providing unified document loaders, embedding models, text splitters, and vector databases in one package.
* Retriever and Rerankers coming soon
* Langchain based

## **BENEFITS**
* Unified Interface: Simplifies complex processes by providing a unified interface for various RAG utilities.
* Flexibility: Supports multiple document sources, splitting methods, embedding providers, and vector databases, enhancing adaptability to diverse use cases.
* Scalability: Designed to accommodate future functionalities, ensuring long-term viability and relevance.

## **INSTALL AND RUN**
    pip install ragutils

### **Document Loaders**
The DocumentLoader class is used to load documents from different sources and return them as a list of strings. The supported sources include CSV, JSON, PDF, HTML, Markdown, powerpoint and Word documents.

The purpose of the DocumentLoader class is to provide a single interface for loading documents from various sources and to ensure that the process of loading documents is consistent across different sources. This allows the code that uses the DocumentLoader class to be more flexible and easier to maintain.

By using the DocumentLoader class, the code can be written in a way that is independent of the specific source of the document. This makes it easier to modify or extend the code in the future, as new sources of documents can be added without affecting the rest of the code.

#### Example usage:
    from ragutils.document_loader import DocumentLoader
    loader = DocumentLoader()
    file_path = os.path.join("path/to/file.csv")
    data = loader.load_and_split(file_path)
    url = "https://example.com/document.html"
    data = loader.load(url)

### **Text Splitters**
The TextSplitter class is used to split text into a list of document objects. It can be used to preprocess the text data before indexing it to a vector database.

The TextSplitter class provides a number of different splitters, including splitters that split based on HTML headers, Markdown headers, character boundaries, recursive character boundaries, and semantic chunks. The splitters can be configured with arguments to control the splitting process, such as the maximum length of the chunks or the set of headers to split on.

The TextSplitter class is designed to be flexible and can be used with a wide range of text data, including HTML documents, Markdown documents, and plain text. It is also designed to be scalable in future.

#### Example usage:
    from ragutils.document_loaders import DocumentLoader
    from ragutils.text_splitter import TextSplitter
    document_loader = DocumentLoader()
    splitter = TextSplitter(splitter="recursive")

    file_path = os.path.join("path/to/file.csv")
    data = loader.load_and_split(file_path)
    documents = splitter.split_to_documents(data= data, chunk_size = 1000, chunk_overlap=20 )

### **Embedding Providers**
The EmbeddingProvider class is responsible for providing different embedding functions based on the embedding_provider specified in the settings file. It initializes the class with the specified embedding_provider and provides the get_embedding_function method to retrieve the embedding function based on the model_name.

#### Example usage:
    from ragutils.document_loader import DocumentLoader
    from ragutils.text_splitter import TextSplitter
    from ragutils.embedding_provider import EmbeddingProvider

    loader = DocumentLoader()
    file_path = os.path.join("path/to/file.csv")
    data = loader.load_and_split(file_path)
    url = "https://example.com/document.html"
    data = loader.load(url)

    # Split the text
    splitter = TextSplitter(splitter="recursive")
    documents = splitter.split_to_documents(data=data, chunk_size=1000, chunk_overlap=20)

    # Get the embedding function
    embedding_provider = EmbeddingProvider(embedding_provider="openai")
    embedding_function = embedding_provider.get_embedding_function()

#### **Vector Databases**
The purpose of the VectorDatabase class is to manage different vector databases, such as Chroma, Pinecone, Milvus, Qdrant, DocArrayInMemorySearch, and Faiss. It provides a consistent interface for creating and managing indexes for different vector databases.

#### Example usage
    from ragutils.document_loader import DocumentLoader
    from ragutils.text_splitter import TextSplitter
    from ragutils.embedding_provider import EmbeddingProvider
    from ragutils.vector_databases import VectorDatabase

    loader = DocumentLoader()
    file_path = os.path.join("path/to/file.csv")
    data = loader.load_and_split(file_path)
    url = "https://example.com/document.html"
    data = loader.load(url)

    # Split the text
    splitter = TextSplitter(splitter="recursive")
    documents = splitter.split_to_documents(data=data, chunk_size=1000, chunk_overlap=20)

    # Get the embedding function
    embedding_provider = EmbeddingProvider(embedding_provider="openai")
    embedding_function = embedding_provider.get_embedding_function()

    #embed the documents
    index_dir = 'tests/index/'
    vector_database = VectorDatabase(vector_store='chroma', index_name='test_index')
    vector_database.create_index(embedding_function, documents, index_dir)

### **Retrievers (Coming Soon)**
Stay tuned for retriever functionalities.

### **Rerankers (Coming Soon)**
Stay tuned for reranker functionalities.

## **CONTRIBUTE**
Feel free to contribute to ragutils by submitting bug reports, feature requests, or pull requests on GitHub.

