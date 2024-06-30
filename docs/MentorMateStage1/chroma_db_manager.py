import chromadb
from custom_pdf_loader import CustomPDFLoader

class ChromaDBManager:
    def __init__(self, db_path):
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        self.collection = None
        self.pages = None  # Initialize pages attribute

    def setup_collection(self, collection_name):
        try:
            self.chroma_client.delete_collection(name=collection_name)
        except Exception as e:
            if "does not exist" not in str(e):
                raise e  # Reraise unexpected Exception
            # Collection doesn't exist, continue
            pass

        self.collection = self.chroma_client.create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def load_documents(self, pdf_file):
        loader = CustomPDFLoader(pdf_file)
        self.pages = loader.load()  # Store loaded pages in self.pages
        return self.pages
    
    def add_documents_to_collection(self, pages):
        if not self.collection:
            raise ValueError("Collection is not set up. Call setup_collection() first.")
        
        for page in pages:
            self.collection.add(
                documents=[page.page_content],
                ids=[str(page.metadata['page'])],
                metadatas=[page.metadata]
            )

    def query_documents(self, query_texts, n_results=2):
        if not self.collection:
            raise ValueError("Collection is not set up. Call setup_collection() first.")
        
        results = self.collection.query(
            query_texts=query_texts,
            n_results=n_results
        )
        return results['documents']

    # method to add data to the vector database at once
    def add_data_to_vectorDb(self, collection_name, data_path):
        self.setup_collection(collection_name)
        documents = self.load_documents(data_path)
        self.add_documents_to_collection(documents)
        
        