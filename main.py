from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# Here {Topic is placeholder}
template = "Write a short poem about {Topic}"

prompt = PromptTemplate(input_variables=["Topic"], template=template)

final_prompt = prompt.format(Topic="Flower")

# when use invoke we have the pass the dictionary instead of argument
# And in case of invode we get object as output but when give prompt to llm there is no difference
# final_prompt = prompt.invoke({"Topic": "Flower"})

llm = ChatOllama(
    model="llama3.2"
)

response = llm.invoke(
    "Explain LangChain in simple terms."
)

print(response.content)