from chroma_db_manager import ChromaDBManager
from mentor_mate import mentorMate

user_input = "what are the primary branches of biology?"

# creating chromaDB client to access the vector database
vectorDB = ChromaDBManager("vectorDb")

# adding data to the vector database using chroma client
vectorDB.add_data_to_vectorDb('IntroToBio', 'testData/IntroToBio.pdf')


# query the vector database to get the similar documents using current chromadb client
similarity_docs = vectorDB.query_documents(user_input)

mentor = mentorMate(user_input, similarity_docs)
response = mentor.get_response()

print(response)





