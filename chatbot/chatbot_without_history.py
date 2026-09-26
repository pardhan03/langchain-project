from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)


print("Chat started. Type your message below. Type 'exit' or 'quit' to stop.\n")

while True:
    print("=" * 50)
    user_input = input("Enter: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bye")
        break

    user_prompt = """
        Provide short responses.
        You are expert in python.

        {user_input}
    """
    prompt = PromptTemplate.from_template(user_prompt)

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"user_input": user_input})

    print(f"User: {user_input}")
    print(f"Response: {response}")