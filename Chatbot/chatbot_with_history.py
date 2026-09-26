from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2"
)


prompt = """
Provide short responses.
You are expert in python.
"""
system_prompt = SystemMessage(prompt)
messages: list[SystemMessage | HumanMessage | AIMessage] = [system_prompt]

print("Chat started. Type your message below. Type 'exit' or 'quit' to stop.\n")

while True:
    print("=" * 50)
    user_input = input("Enter: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bye")
        break

    human_prompt = HumanMessage(user_input)
    messages.append(human_prompt)

    response: AIMessage = llm.invoke(messages)
    messages.append(response)

    print(f"User: {user_input}")
    print(f"Response: {response.content}")