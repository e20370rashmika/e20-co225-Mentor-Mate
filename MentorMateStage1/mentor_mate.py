from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv



class mentorMate:
    def __init__(self, user_input, similarity_doc):
        self.user_input = user_input
        self.similarity_doc = similarity_doc
        load_dotenv()

    def get_response(self):
        llm = ChatGroq(temperature=0.4,
                    max_tokens=1000,
                    model="Llama3-8b-8192",
                    streaming=True,)

        system = """your are a helpfull personal tutor. your task is to answer questions about biology based on the content provided.
                your scope is limited to the content provided. you'are answering to a advanced level high school student.
                    Answer the following question: {question}
                    By searching the following content: {transcript}
                    Only use the factual information from the content to answer the question.
                    If you feel like you don't have enough information to answer,say "I don't have enough information to answer this question" 
                    your answer should be detailed and informative. First give a short answer using 2-3 sentences, then provide more details and explanations.
                    Always refer to the content provided when answering questions.This content is your primary knowledge base.    
                """
        chat_template = ChatPromptTemplate.from_messages([("system", system)])
        

        chain = chat_template | llm
        response = chain.invoke(
                {"question":self.user_input,
                "transcript":self.similarity_doc}
            )

        return self.clean_text(response.content)
    
    def clean_text(self,text):
        # method to clean the text content of the page_content field in the Document object
        # Replace new lines with spaces
        text = text.replace('\n', ' ')
        # Split by whitespace and re-join to remove extra spaces
        text = ' '.join(text.split())
        return text

