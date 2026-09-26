from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser

llm = ChatOllama(
    model="llama3.2"
)

parser = StrOutputParser()

list_parser = CommaSeparatedListOutputParser()

prompt = ChatPromptTemplate.from_template("List the three cities that start with letter {letter}")

final_prompt = prompt.format(letter="P")

# Comma seperate list parser

format_instructions  = CommaSeparatedListOutputParser.get_format_instructions()
print(format_instructions)

# Without get_format_instructions
# In the prompt we have to tell

# from langchain_core.output_parsers import CommaSeparatedListOutputParser
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate

# # Set up the LLM
# llm = ChatOpenAI(model="gpt-4o-mini")

# # Use the JSON Output Parser
# parser = CommaSeparatedListOutputParser()

# # Define your prompt template
# template = "List three {item_type}. Provide in comma separated values."
# prompt = PromptTemplate.from_template(template=template)

# # Parse the LLM response
# chain = prompt | llm | parser

# response = chain.invoke({"item_type": "unique ai models"})
# print(response)
# print(type(response))

list_prompt = ChatPromptTemplate.from_template("List three {item_type}. /n/n{format_instructions}")

# What .partial() does

# You already know the value of format_instructions:
# format_instructions = CommaSeparatedListOutputParser.get_format_instructions()
# So instead of passing it every single time, you can permanently/pre-fill it into the prompt:

# list_prompt_partial = list_prompt.partial(
#     format_instructions=format_instructions
# )

# Only {item_type} is still waiting.
# So later you can simply do:

# list_prompt_partial.invoke({
#     "item_type": "cities"
# })

# partial - We can fill some value beforehand
list_prompt_partial = list_prompt.partial(format_instructions=format_instructions)

# Build the LCEL Chain
list_chain = list_prompt_partial | llm | list_parser

response = llm.invoke(final_prompt)

result_str = parser.parse(response.content)
print(result_str)

# Invoke the chain
result_list = list_chain.invoke({"item_type": "unique ai models"})

# In this case we don't need to format the prompt also
# This is called LECL(Landchain express language) Chain: Prompt | Model | Parser

# chain = prompt | llm | parser
# result_str = chain.invoke({ "letter": "P"})