from fastapi import FastAPI
from src.routes import base
from src.routes import Chatbot
from src.routes import data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(Chatbot.chat_router)
app.include_router(data.data_router)
