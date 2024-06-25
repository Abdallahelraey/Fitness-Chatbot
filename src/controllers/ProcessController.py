from .BaseController import BaseController
from src.utils.config import get_settings, Settings
from src.models import BaseDataModel
from langchain_groq import ChatGroq
from src.models import BaseDataModel
from typing import List, Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory # For reliable memory usage
# from langchain_huggingface import ChatGroq  # Updated import


class ProcessController(BaseController):
    def __init__(self):
        super().__init__()
        self.app_settings = get_settings()
        self.db_dir = self.app_settings.DB_DIR
        self.model = BaseDataModel()
        self.processed_docs = set()  # Keep track of processed documents
        # self.memory = ConversationBufferMemory()  # Initialize memory
        self.memory = ConversationBufferWindowMemory(k=10)
        self.conversation_history = self.memory.load_memory_variables({}) # Retrieve the conversation history

    def ensure_document_processed(self, doc_name: str) -> None:
        if doc_name not in self.processed_docs:
            self._load_and_prepare_documents(doc_name)
            self.processed_docs.add(doc_name)

    def _load_and_prepare_documents(self, doc_name: str) -> None:
        documents = self.model.load_documents(doc_name)
        chunks = self.model.split_text(documents)
        self.model.save_to_chroma(chunks,doc_name)

    def _search_documents(self, query_text: str) -> List[Any]:
        return self.model.search_chroma_db(query_text)

    def _generate_response(self, query_text: str, results: List[Any]) -> str:

        # Generate the prompt using the model's generate_prompt method
        prompt = self.model.generate_prompt(query_text, results, memory=str(self.memory))
        
        # Generate the response using the model
        groq_model = ChatGroq(temperature=0, model_name="llama3-70b-8192")  # Adjust model as necessary =>  mixtral-8x7b-32768
        response = groq_model.invoke(prompt)
        
        self.memory.save_context({"input": query_text}, {"output": response.content})
        
        return response.content


    def process_query(self, doc_name: str, query_text: str) -> Dict[str, Any]:
        self.ensure_document_processed(doc_name)
        results = self._search_documents(query_text)
        if not results:
            return {
                "result": "Unable to find matching results.",
                "source_documents": [],
                "scores": []
            }
        displayed_response = self._generate_response(query_text, results)
        sources = "\n\n---\n\n".join(["\n".join(result) for result in results])
        return {
            "result": displayed_response,
            "source_documents": sources,
        }