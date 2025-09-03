from langchain_groq import ChatGroq
import streamlit as st

class GroqLLM:

    def __init__(self,user_actions):
        self.user_actions =user_actions
    
    def get_groq_llm(self):
        model = self.user_actions["GROQ_MODEL"]
        groq_api_key = self.user_actions["GROQ_API_KEY"]
        
        try:
           model = self.user_actions["GROQ_MODEL"]
           groq_api_key = self.user_actions["GROQ_API_KEY"]
           if groq_api_key == '':
              st.error("Please enter Groq API key")
           llm = ChatGroq(model=model,groq_api_key=groq_api_key)

        except Exception as e:
            print(e)
        return llm 