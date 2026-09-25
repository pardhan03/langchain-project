from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)

response = llm.invoke(
    "Explain LangChain in simple terms."
)

print(response.content)