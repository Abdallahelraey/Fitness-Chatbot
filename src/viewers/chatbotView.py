
            
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

        # Radio button to select the document name
        doc_name = st.radio(
            "Choose a document:",
            ("fitness.txt", "health.txt"),
            index=0
        )

        query = st.text_input("Enter your query:")

        if st.button("Submit"):
            if doc_name and query:
                try:
                    response = self.controller.process_query(doc_name, query)
                    if isinstance(response, dict):
                        st.write(response["result"])
                        st.write("Knowledge Base Below")
                        st.write(response["source_documents"])
                    else:
                        st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please select a document and enter a query.")