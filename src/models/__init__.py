from src.utils.config import get_settings, Settings

class BaseDataModel:

    def __init__(self):
        self.app_settings = get_settings()
    
    