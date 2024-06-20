from .BaseController import BaseController
from src.utils.config import get_settings, Settings
from src.models import BaseDataModel
from langchain_groq import ChatGroq
from src.models import BaseDataModel

class ProcessController(BaseController):

    def __init__(self):
        super().__init__()
        self.app_settings = get_settings()
        self.db_dir = self.app_settings.DB_DIR
        self.model = BaseDataModel()

    def process_query(self, doc_name, query_text):
        documents = self.model.load_documents(doc_name)
        chunks = self.model.split_text(documents)
        self.model.save_to_chroma(chunks)

        results = self.model.search_chroma_db(query_text)
        if not results:
            return "Unable to find matching results."

        prompt = self.model.generate_prompt(query_text, results)
        groq_model = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
        response_text = groq_model.invoke(prompt)

        sources = [doc.metadata.get("source", None) for doc, _score in results]
        formatted_response = f"Response: {response_text}\nSources: {sources}"


        #return formatted_response
        return {
            "result": response_text,
            "source_documents": [doc for doc, _score in results]
        }