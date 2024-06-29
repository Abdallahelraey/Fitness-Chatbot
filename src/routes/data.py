from fastapi import FastAPI, APIRouter, Depends, UploadFile, File, HTTPException
from src.utils.config import get_settings, Settings
from src.controllers import DocumentController
import aiofiles
import os

app = FastAPI()

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

document_controller = DocumentController()

UPLOAD_DIRECTORY = document_controller.files_dir

@data_router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), settings: Settings = Depends(get_settings)):
    # Log the incoming file data
    print(f"Received file: {file.filename}, Content-Type: {file.content_type}")

    # Validate the uploaded file
    is_valid, validation_message = document_controller.validate_uploaded_file(file)
    if not is_valid:
        raise HTTPException(status_code=400, detail=validation_message)

    file_path = document_controller.get_project_path(Doc_name=file.filename)
    
    # Check if the file already exists
    if os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="FILE_ALREADY_EXISTS")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    async with aiofiles.open(file_path, "wb") as out_file:
        while content := await file.read(1024):  # Read the file in chunks
            await out_file.write(content)
    
    return {"filename": file.filename}


