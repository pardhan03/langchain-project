from langchain_core.runnables import RunnableLambda


def reverse(s: str) -> str:
    # A simple Python function to reverse a string
    return s[::-1]

def convert_title(s: str) -> str:
    # 2. Converts the string to Title Case
    return s.title()


# Wrap the function to turn it into a Runnable
# runnable = RunnableLambda(func=reverse)


runnable_1 = RunnableLambda(func=reverse)
runnable_2 = RunnableLambda(func=convert_title)

chain = runnable_1 | runnable_2


# Invoke the Runnable directly
print(f"Output: {chain.invoke('Hello')}")

# olleH
# Output: Olleh