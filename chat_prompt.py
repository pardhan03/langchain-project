from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
# When use open ai package/sdk
# system
# user
# assistant

# In langchain
# system
# human
# ai

llm = ChatOllama(
    model="llama3.2"
)

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are very helpful assistant that speak like a {persona}"),
        ("human", "Explain {concept} in one sentence")
    ]
)

message = chat_template.format(persona = "18th century pirate", concept = "recursion")
print(message)

response = llm.invoke(message)
print(response.content)