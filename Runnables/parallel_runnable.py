from langchain_core.runnables import RunnableLambda, RunnableParallel

def add_ten(x: dict) -> dict:
    return { "added": x["input"] + 10}

def add_one(x: int) -> int:
    return x + 1


def mul_two(x: int) -> int:
    # Takes the output of add_one (2) and multiplies it
    return x * 2


def mul_three(x: int) -> int:
    # Takes the output of add_one (2) and multiplies it
    return x * 3

# Now in RunnableParallel instead like RunabblePassthrough in which we send the output to the next step
# In this we execute both step at the same time without passing any value
mapper = RunnableParallel(
    {
        "add_step": RunnableLambda(add_ten),
        "add_step2": RunnableLambda(add_ten),
    }
)

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
runnable_3 = RunnableLambda(mul_three)

# Chain Breakdown:
# 1. runnable_1 gets 1, outputs 2.
# 2. The dictionary acts as a RunnableParallel:
#    It takes 2 as input and sends it to runnable_2 and runnable_3 simultaneously.
# Note: RunnableParallel can be created with either dictionary syntax or keyword args.

# Using dictionary syntax in LCEL:
# runnable_1 value will pass to the both runnables in the dict
chain_dict = runnable_1 | {"mul_two": runnable_2, "mul_three": runnable_3} # RunnableParallel passthrough
print(f"Output: {chain_dict.invoke(1)}") # Output: {'mul_two': 4, 'mul_three': 6}

print(f"Output: { mapper.invoke({ 'input': 10})}")