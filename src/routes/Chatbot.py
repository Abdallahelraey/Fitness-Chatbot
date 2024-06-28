from fastapi import FastAPI, HTTPException,APIRouter, Depends
from pydantic import BaseModel, EmailStr , field_validator
from typing import List, Optional
from src.controllers import ProcessController
# from src.controllers import DocumentController
import uvicorn

chat_router = APIRouter(
    prefix="/api/v1/chatbot",
    tags=["api_v1", "chatbot"],
)
process_controller = ProcessController()
# document_controller = DocumentController()


class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    prompt: str
    history: List[ChatMessage]
    email: EmailStr
    password: str
    doc_name: str

class UserRequest(BaseModel):
    email: EmailStr
    password: str

class DocRequest(BaseModel):
    doc_name: str
    @field_validator('doc_name')
    def check_doc_name(cls, v):
        if v not in {"health.txt", "fitness.txt"}:
            raise ValueError('Invalid document name')
        return v

@chat_router.post("/document/")
async def get_document(doc_request: DocRequest):
    
    try:
        # document_controller.validate_doc(doc_request)
        return {"message": "Document processed successfully", "doc_name": doc_request.doc_name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@chat_router.post("/user/")
async def get_user(user_request: UserRequest):
    try:
        process_controller.ingest_user_data(email=user_request.email, password=user_request.password)
        return {"message": "User data ingested successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@chat_router.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # Ensure user data is ingested
        process_controller.ingest_user_data(email=request.email, password=request.password)
        # Store the user data (optional, if needed)
        response = process_controller.process_query(request.doc_name, request.prompt)
        return {"result": response["result"]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))