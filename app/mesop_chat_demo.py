import random
import time

import mesop as me
import mesop.labs as mel
from src.controllers import ProcessController
from src.utils.config import get_settings, Settings
from typing import List, Dict, Any




settings = get_settings()
db_dir = settings.DB_DIR
process_controller = ProcessController()


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/chat",
  title="AI Fitness Coach",
)
def chat():
  mel.chat(transform, title="X Fit", bot_user="Fitness Coach")


# def transform(prompt: str, history: List[mel.ChatMessage]) -> str:
#     history_string = ""
#     for m in history:
#         history_string += f"{m.role}: {m.content}\n"
    
#     doc_name = "health.txt"  # Replace with your actual document name or logic to select it
#     response = process_controller.process_query(doc_name, prompt)
    
#     return response["result"]

def transform(prompt: str, history: List[mel.ChatMessage]) -> str:
    history_string = process_controller.conversation_history
    
    doc_name = "health.txt"  # Replace with your actual document name or logic to select it
    response = process_controller.process_query(doc_name, prompt)
    
    return response["result"]