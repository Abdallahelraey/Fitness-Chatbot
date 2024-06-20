from src.utils.config import get_settings, Settings
from src.controllers import DocumentController
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
import shutil
import os


class BaseDataModel:

    def __init__(self):
        self.app_settings = get_settings()
        self.db_dir = self.app_settings.DB_DIR
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.DocumentController = DocumentController()

    def load_documents(self, doc_name):
        file_abs_path = self.DocumentController.get_project_path(Doc_name=doc_name)
        loader = TextLoader(file_abs_path)
        documents = loader.load()
        return documents

    def split_text(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
        )
        chunks = text_splitter.split_documents(documents)
        return chunks

    def save_to_chroma(self, chunks):
        if os.path.exists(self.db_dir):
            shutil.rmtree(self.db_dir)
        db = Chroma.from_documents(chunks, self.embeddings, persist_directory=self.db_dir)
        db.persist()
        print(f"Saved {len(chunks)} chunks to {self.db_dir}.")

    def search_chroma_db(self, query_text):
        db = Chroma(persist_directory=self.db_dir, embedding_function=self.embeddings)
        results = db.similarity_search_with_relevance_scores(query_text, k=3)
        if len(results) == 0 or results[0][1] < 0.2:
            print(f"Unable to find matching results.")
            return []
        return results

    def generate_prompt(self, query_text, results):
        PROMPT_TEMPLATE = """
        Answer the question based only on the following context:
        {context}
        ---
        Answer the question based on the above context: {question}
        """
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
        return prompt
        