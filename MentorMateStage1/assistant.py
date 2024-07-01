#this file contains the main functions for the youtube assistant project . use this for refernce when creating the mentor mate project
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores  import FAISS
from langchain_community.embeddings import JinaEmbeddings
from langchain_ai21 import AI21SemanticTextSplitter
import youtube_transcript as yt


load_dotenv()



#embeddings = OpenAIEmbeddings()
embeddings = JinaEmbeddings(
     model_name="jina-embeddings-v2-base-en"
)

def create_vector_db_from_youtube(url) -> FAISS:

#    loader = YoutubeLoader.from_youtube_url(url)
#    transcript = loader.load()
#    text = transcript[0].page_content

    text = yt.youtube_transcript_from_url(url)

    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,o)
    semantic_text_splitter = AI21SemanticTextSplitter(chunk_size=1000,chunk_overlap=100)
    docs= semantic_text_splitter.split_text_to_documents(text)    
    #docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs,embeddings)
  
    return db
    
    
def youtube_assistant(user_input,db,k=4):

    docs = db.similarity_search(user_input,k=k)
    similarity_doc = " ".join(str(doc) for doc in docs)

    llm = ChatGroq(temperature=0.4,
                   max_tokens=1000,
                   model="Llama3-8b-8192",
                   streaming=True,)
    

    system = """your are a helpfull youtube assistant. your task is to answer questions about videos based on the video's trnascript
                Answer the following question: {question}
                By searching the following transcript: {transcript}
                Only use the factual information from the transcript to answer the question.
                If you feel like you don't have enough information to answer,say "I don't have enough information to answer this question" 
                your answer should be detailed and informative. First give a short answer using 2-3 sentences, then provide more details and explanations.
                Always refer to the video's transcript when answering questions.
                
            """
    chat_template = ChatPromptTemplate.from_messages([("system", system)])
    

    chain = chat_template | llm
    response = chain.invoke(
        {"question":user_input,
        "transcript":similarity_doc}
    )

    return response.content
    
    



    


    

