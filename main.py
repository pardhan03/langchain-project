from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate

examples = [
    { "input": "happy", "output": "sad"},
    { "input": "tall", "output": "short"},
    { "input": "sunny", "output": "gloomy"},
]

# Here {Topic is placeholder}
template = "Write a short poem about {Topic}"

prompt = PromptTemplate(input_variables=["Topic"], template=template)

# Easy way of writing above piece of code
# prompt = PromptTemplate.from_template(
#     "Write a short poem about {Topic}"
# )

final_prompt = prompt.format(Topic="Flower")

# when use invoke we have the pass the dictionary instead of argument
# And in case of invode we get object as output but when give prompt to llm there is no difference
# final_prompt = prompt.invoke({"Topic": "Flower"})

# When use open ai package/sdk
# system
# user
# assistant

# In langchain
# system
# human
# ai


# This type of prompting also known as zero short prompting because here
# we didn't give any context to llms
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are very helpful assistant that speak like a {persona}"),
        ("human", "Explain {concept} in one sentence")
    ]
)

message = chat_template.format_messages(persona = "18th century pirate", concept = "recursion")
print(message)

example_template = PromptTemplate(
    input_variables=["input", "output"],
    template="Word: {input}\nAntonym: {output}"
)

few_short_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    prefix="Give the antonym of every word provided.", # Instruction at the start
    suffix="Word: {user_input}\nAntonym",
    input_variables=["user_input"]
)

few_short_prompt_message = few_short_prompt.format(user_input = "big")
print(few_short_prompt.format(user_input="big"))


llm = ChatOllama(
    model="llama3.2"
)

response = llm.invoke(
    "Explain LangChain in simple terms."
)



prompt_template_response = llm.invoke(message)

few_short_template_response = llm.invoke(few_short_prompt_message)

print(response.content)

print(prompt_template_response.content)

print(few_short_template_response.content)
