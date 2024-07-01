
from langchain_community.document_loaders import PyPDFLoader

class CustomPDFLoader(PyPDFLoader):
    def __init__(self,path):
        super().__init__(path)

    #overwriting the load method from PyPDFLoader
    def load(self,extract_images=True):
        #This method will return a list of Document objects from Langchain core wiht cleaned text in page_content
        #load the pages using parent class method and then clean the text

        documents = super().load()

        #cleaning text after loading
        for doc in documents:
            doc.page_content = self.clean_text(doc.page_content)
        return documents
    
    # overwriting the method load_and_split() from PyPDFLoader
    def load_and_split(self):
        #This method will return a list of Document objects from Langchain core with cleaned text in page_content
        #load the pages using parent class method and then clean the text

        documents = super().load_and_split()

        #cleaning text after loading
        for doc in documents:
            doc.page_content = self.clean_text(doc.page_content)
        return documents
    
    def clean_text(self,text):
        # method to clean the text content of the page_content field in the Document object
        # Replace new lines with spaces
        text = text.replace('\n', ' ')
        # Split by whitespace and re-join to remove extra spaces
        text = ' '.join(text.split())
        return text
    
    def get_page(self,page_number):
        # method to get the page content of a specific page number
        pages = self.load()
        for page in pages:
            if page.metadata['page']==page_number:
                return page.page_content
        print("Page not found")
        return None

