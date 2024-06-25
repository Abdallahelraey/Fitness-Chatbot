from .BaseController import BaseController
from src.utils.config import get_settings, Settings
from src.models import BaseDataModel
from langchain_groq import ChatGroq
from src.models import BaseDataModel
from typing import List, Dict, Any

class ProcessController(BaseController):
    def __init__(self):
        super().__init__()
        self.app_settings = get_settings()
        self.db_dir = self.app_settings.DB_DIR
        self.model = BaseDataModel()
        self.processed_docs = set()  # Keep track of processed documents

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
        prompt = self.model.generate_prompt(query_text, results)
        groq_model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
        response = groq_model.invoke(prompt)
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
        sources = "\n\n---\n\n".join([ "\n".join(result) for result in results ])
        return {
            "result": displayed_response,
            "source_documents": sources,
        }
        