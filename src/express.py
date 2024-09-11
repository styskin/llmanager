from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model_name="gpt-4o"
)

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

messages = [
    SystemMessage(content="You are ExpertGPT, an AGI system capable of everything")
]

messages.append(
    HumanMessage(
        content="Hey how are you doing today? What is the meaning of life?"
    )
)
res = llm(messages)
print(res)