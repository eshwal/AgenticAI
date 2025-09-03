from src.langgraph_agent.state.chatbot_state import ChatBotState


class GraphNode:
    
    def __init__(self,model):
        self.llm = model

    def  chatbot (self,state: ChatBotState)-> ChatBotState:
        return {'messages': self.llm.invoke(state["messages"])}
