#This script is used to update the vector database with the data from the pdf files in the testData folder
#The script uses the ChromaDBManager class from chroma_db_manager.py to vreate chroma client andadd data to the vector database

from chroma_db_manager import ChromaDBManager

# creating chromaDB client to access (add data to) the vector database
vectorDB = ChromaDBManager("vectorDb")

# adding data to the vector database using chroma client
vectorDB.add_data_to_vectorDb('IntroToBio', 'testData/IntroToBio.pdf')
