from langchain_experimental.tools import PythonREPLTool

python_tool = PythonREPLTool()

code_input = """
def hello():
    print("Hello world!")
hello()
"""

result = python_tool.invoke(code_input)

print(result)