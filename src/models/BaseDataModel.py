from src.utils.config import get_settings, Settings
from src.controllers import DocumentController
from typing import List, Dict, Any
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
import chromadb.utils.embedding_functions as embedding_functions
import chromadb
import uuid
import os


class BaseDataModel:

    def __init__(self):
        self.app_settings = get_settings()
        self.db_dir = self.app_settings.DB_DIR
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.DocumentController = DocumentController()

    def load_documents(self, doc_name):
        file_abs_path = self.DocumentController.get_project_path(Doc_name=doc_name)
        loader = TextLoader(file_abs_path, encoding="utf-8")
        documents = loader.load()
        return documents

    def split_text(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=200,
            chunk_overlap=50,
            length_function=len,
            add_start_index=True,
        )
        chunks = text_splitter.split_documents(documents)
        return chunks

    def embedding_function_huggingface(self):
        huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=self.app_settings.HUGGING_FACE_API_KEY,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        return huggingface_ef

    def derive_collection_name(self, doc_name):
        # Derive collection name from document name (e.g., "example_document.txt" -> "example_document")
        collection_name = doc_name.split('.')[0]
        return collection_name

    def save_to_chroma(self, chunks, doc_name):
        collection_name = self.derive_collection_name(doc_name)
        chroma_client = chromadb.PersistentClient(path=self.db_dir)
        embedding_function = self.embedding_function_huggingface()
        collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)
        document_ids = [str(uuid.uuid4()) for _ in chunks]
        collection.upsert(
            documents=[doc.page_content for doc in chunks ],
            ids=document_ids
        )

    def search_chroma_db(self,doc_name ,query_text):
        chroma_client = chromadb.PersistentClient(path=self.db_dir)
        embedding_function = self.embedding_function_huggingface()
        collection_name = self.derive_collection_name(doc_name)
        collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)
        results = collection.query(
        query_texts=[query_text], # Chroma will embed this for you
        n_results=5 # how many results to return
        )
        return  results["documents"]
        # return {
        # "results_documents": results["documents"],
        # "results_distances": results["distances"]
        # }
          
    def generate_prompt(self, query_text, results, memory):
        PROMPT_TEMPLATE = """
        You are a fitness coach for the XFit Organization with a knowledge base that supports your answers.
        Answer the question based on the following context and conversation history:
        {memory}
        
        Context from Knowledge base documents This is the part you have to give emphases to more than the conversation history:
        {context}
        
        ---
        Answer the question based on the above context: {question}
        """
        context_text = "\n\n---\n\n".join(["\n".join(result) for result in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(memory=memory, context=context_text, question=query_text)
        return prompt