from langchain_core.runnables import RunnableLambda, RunnablePassthrough


def reverse(s: str) -> str:
    return s[::-1]


def convert_title(_dict: dict[str, str]) -> dict:
    # This function now takes the dictionary output from the previous step
    # and converts it to a title-cased string for display.
    return {"output": _dict["output"].title(), "temp": _dict}


runnable_1 = RunnableLambda(func=reverse)
runnable_2 = RunnableLambda(func=convert_title)

# Chain Breakdown:
# 1. runnable_1 gets "Hello" and outputs "olleH".
# 2. {"output": RunnablePassthrough()} takes "olleH" (the input to this step)
#    and creates a dictionary: {"output": "olleH"}.
# 3. runnable_2 gets the dictionary {"output": "olleH"}.
chain = runnable_1 | {"output": RunnablePassthrough(), "output_2": RunnablePassthrough()} | runnable_2


print(f"Output: {chain.invoke('Hello')}")