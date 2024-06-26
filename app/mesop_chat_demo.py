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

@me.stateclass
class State:
  health: str = "health.txt"
  fitness: str = "fitness.txt"
  doc_name: str = "health.txt"  # default value
  agent_name = "XFit Health Coach"

def health_button_click(action: me.ClickEvent):
  state = me.state(State)
  state.doc_name  = state.health 
  state.agent_name = "XFit Health Coach"
    
def fitness_button_click(action: me.ClickEvent):
  state = me.state(State)
  state.doc_name  =state.fitness 
  state.agent_name = "XFit Fitness Coach"


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/",
  title="AI Fitness Coach",
)
def chat():
  state = me.state(State)
  me.button("General Health", on_click=health_button_click)
  me.button("Fitness", on_click=fitness_button_click)
  mel.chat(transform, title="X Fit", bot_user=state.agent_name)


def transform(prompt: str, history: List[mel.ChatMessage]) -> str:
    state = me.state(State)
    history_string = process_controller.conversation_history
    
    doc_name = state.doc_name  
    # Example usage
    email = "AbdullahGom3a@gmail.com",
    password ="gom3a2001"
    process_controller.ingest_user_data(email=email , password=password)
    response = process_controller.process_query(doc_name, prompt)
    # detailed_response = detailed_response = response["result"] + "\n" + response["source_documents"]
    # return detailed_response
    return response["result"]