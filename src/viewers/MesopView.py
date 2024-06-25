
# Mesop View

from src.controllers import ProcessController
from src.utils.config import get_settings, Settings

import random
import time
import mesop as me
import mesop.labs as mel


class MesopView:
    def __init__(self):
        settings = get_settings()
        self.db_dir = settings.DB_DIR
        self.controller = ProcessController()
        self.LINES = [
            "Mesop is a Python-based UI framework designed to simplify web UI development for engineers without frontend experience.",
            "It leverages the power of the Angular web framework and Angular Material components, allowing rapid construction of web demos and internal tools.",
            "With Mesop, developers can enjoy a fast build-edit-refresh loop thanks to its hot reload feature, making UI tweaks and component integration seamless.",
            "Deployment is straightforward, utilizing standard HTTP technologies.",
            "Mesop's component library aims for comprehensive Angular Material component coverage, enhancing UI flexibility and composability.",
            "It supports custom components for specific use cases, ensuring developers can extend its capabilities to fit their unique requirements.",
            "Mesop's roadmap includes expanding its component library and simplifying the onboarding processs.",
        ]

    @me.page(
        security_policy=me.SecurityPolicy(
            allowed_iframe_parents=["https://google.github.io"]
        ),
        path="/chat",
        title="AI Fitness Coach",
    )
    def page(self):
        mel.chat(self.transform, title="X Fit", bot_user="Fitness Coach")

    def transform(self, input: str, history: list[mel.ChatMessage]):
        for line in random.sample(self.LINES, random.randint(3, len(self.LINES) - 1)):
            time.sleep(0.3)
            yield line + " "