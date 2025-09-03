from src.langgraph_agent.ui.uiconfig import Config
import streamlit as st

class UILoader:
    def __init__(self):
        self.config = Config()
        self.user_selection = {}

    def load_sidebar_ui(self):
        st.title(self.config.get_title())
        self.user_selection['LLM']=st.sidebar.selectbox("Select LLM",self.config.get_LLM())
        if self.user_selection['LLM'] == 'GROQ':
            self.user_selection['GROQ_MODEL'] = st.sidebar.selectbox("Select Model",self.config.get_groq_models())
            self.user_selection['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY'] = st.sidebar.text_input("GROQ_API_KEY",type='password')
        try:
            if self.user_selection['GROQ_API_KEY'] == '' :
                st.sidebar.warning("Please enter API Key")
        except Exception as e:
            print(e)
        self.user_selection['Usecase']=st.sidebar.selectbox("Select Usecase",self.config.get_usecases())
        return self.user_selection
