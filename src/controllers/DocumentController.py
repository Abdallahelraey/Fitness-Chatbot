from src.controllers.BaseController import BaseController
import os

class DocumentController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_project_path(self, Doc_name: str):
        project_dir = os.path.join(
            self.files_dir,
            Doc_name
        )

        return project_dir

    
