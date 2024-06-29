from src.controllers.BaseController import BaseController
import os
from fastapi import UploadFile
class DocumentController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes
    def get_project_path(self, Doc_name: str):
        project_dir = os.path.join(
            self.files_dir,
            Doc_name
        )

        return project_dir

            
    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, "FILE_TYPE_NOT_SUPPORTED"

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, "FILE_SIZE_EXCEEDED"

        return True, "FILE_VALIDATED_SUCCESS"
