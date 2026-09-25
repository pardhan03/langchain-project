from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

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

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are very helpful assistant that speak like a {persona}"),
        ("human", "Explain {concept} in one sentence")
    ]
)

llm = ChatOllama(
    model="llama3.2"
)

response = llm.invoke(
    "Explain LangChain in simple terms."
)

message = chat_template.format_messages(persona = "18th century pirate", concept = "recursion")
print(message)

prompt_template_response = llm.invoke(message)

print(response.content)

print(prompt_template_response.content)
