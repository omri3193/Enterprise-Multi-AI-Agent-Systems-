from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings

from langchain_core.messages import SystemMessage, HumanMessage

def get_response_from_ai_agents(llm_id , query , allow_search ,system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Prepend the system prompt as a SystemMessage
    # query is expected to be a list of strings from the caller
    messages_payload = [SystemMessage(content=system_prompt)]
    for q in query:
        messages_payload.append(HumanMessage(content=q))

    state = {"messages" : messages_payload}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]






