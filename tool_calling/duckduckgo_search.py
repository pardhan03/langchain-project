from pprint import pprint
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

output = search.invoke("What is the latest python version today.")

print(output)