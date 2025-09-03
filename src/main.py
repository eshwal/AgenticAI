from src.langgraph_agent.ui.streamlitui.load import UILoader
from src.langgraph_agent.llms.groq import GroqLLM
from src.langgraph_agent.graph.chatbot_graph import GraphBuilder
from src.langgraph_agent.ui.streamlitui.display import Display
import streamlit as st

def load_main_ui():
    ui = UILoader()
    user_actions = ui.load_sidebar_ui()

    if not user_actions:
        st.error("Failed to load user input from UI")
        return 
    
    print(f"User actions are: {user_actions}")
    prompt = st.chat_input("Say something")
    print(f"USer input is {prompt}")
    if prompt:
        try:

            # Load model
            llm = GroqLLM(user_actions).get_groq_llm()
             
            if not llm:
                st.error("LLM Model cannot be initialised")
            
            print(llm)
            usecase = user_actions.get("Usecase")
            print(f"Usecase is {usecase}")
            workflow = GraphBuilder(llm).setup_graph(usecase=usecase)
            print(workflow)
            Display(usecase,workflow,prompt).display_result_on_ui()
        except Exception as e:
            st.error(f"Error: {e}")

