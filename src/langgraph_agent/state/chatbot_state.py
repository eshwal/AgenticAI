from typing import Annotated,List,TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class ChatBotState(TypedDict):
    messages : Annotated[List[AnyMessage],add_messages]
