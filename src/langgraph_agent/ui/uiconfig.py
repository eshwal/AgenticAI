from configparser import ConfigParser


class Config:

    def __init__(self):
        self.config=ConfigParser()
        self.config.read(".\\src\\langgraph_agent\\ui\\uiconfig.ini")

    def get_title(self):
        return self.config.get('DEFAULT','title')
    
    def get_LLM(self):
        return self.config.get('DEFAULT','llm').split(", ")
    
    def get_groq_models(self):
        return self.config.get('DEFAULT','groq_models').split(", ")
    
    def get_usecases(self):
        return self.config.get('DEFAULT','use_cases').split(", ")

