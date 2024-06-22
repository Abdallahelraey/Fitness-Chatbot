# # CLI View
# from src.controllers import ProcessController
# from src.utils.config import get_settings, Settings

# class ChatbotView:
#     def __init__(self):
#         settings = get_settings()
#         self.db_dir = settings.DB_DIR
#         self.controller = ProcessController()

#     def run(self):
#         doc_name = input("Enter the document name: ")
#         while True:
#             query_text = input("Enter your query (or 'q' to quit): ")
#             if query_text.lower() == 'q':
#                 break
#             response = self.controller.process_query(doc_name, query_text)
#             print(response)
            
            
# Streamlit View
import streamlit as st
from src.controllers import ProcessController
from src.utils.config import get_settings, Settings

class ChatbotView:
    def __init__(self):
        settings = get_settings()
        self.db_dir = settings.DB_DIR
        self.controller = ProcessController()

    def run(self):
        st.title("RAG Chatbot")
        doc_name = st.text_input("Enter the document name:")

        if doc_name:
            query = st.text_input("Enter your query:")

            if st.button("Submit"):
                response = self.controller.process_query(doc_name, query)
                if isinstance(response, dict):
                    st.write(response["result"])
                    st.write(response["source_documents"])
                    st.write(response["scores"])

                else:
                    st.write(response)