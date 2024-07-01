
from mentor_mate import mentorMate
from vectordb_update import vectorDB

while True:
    # getting user input
    print("I'm Your MentorMate, Ask me anything about biology!")
    print("Type 'exit' to quit")

    user_input = input("what you want to know: ")

    if user_input == 'exit':
        break  

    # queriny the vector database using same chroma client from the vectordb_update.py script
    similarity_docs = vectorDB.query_documents(user_input)

    mentor = mentorMate(user_input, similarity_docs)
    response = mentor.get_response()
    print("--------------------response-------------------")
    print("MentorMate: ", response)
    print("-----------------------------------------------")








