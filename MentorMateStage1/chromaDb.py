import chromadb
from custom_pdf_loader import CustomPDFLoader

chroma_client = chromadb.PersistentClient(path="vectorDb")

try:
    chroma_client.delete_collection(name='IntroToBio')
except chromadb.exceptions.CollectionNotFoundError:
    pass  # Collection doesn't exist, ignore the error



collection = chroma_client.create_collection(
                name='IntroToBio', 
                metadata={"hnsw:space": "cosine"}
            )

loader = CustomPDFLoader('testData/IntroToBio.pdf')
pages = loader.load()

for page in pages:
    collection.add(
        documents=[page.page_content],
        ids=[str(page.metadata['page'])],
        metadatas=[page.metadata]
    )


results = collection.query(
    query_texts=["What are the primary branches of biology"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

retrived_docs = results['documents']
print(retrived_docs[0])


