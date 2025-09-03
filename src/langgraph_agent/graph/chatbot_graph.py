from src.langgraph_agent.state.chatbot_state import ChatBotState
from src.langgraph_agent.nodes.chatbot_node import GraphNode
from langgraph.graph import StateGraph,START,END


class GraphBuilder:

    def __init__ (self,model):
        self.graph = StateGraph(ChatBotState)
        self.llm = model


    def build_chatbot_graph(self):
        self.chatbot_node = GraphNode(self.llm)
        self.graph.add_node("chatbot",self.chatbot_node.chatbot)

        # Add edges
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)


    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "CHATBOT":
            self.build_chatbot_graph()
        return self.graph.compile()