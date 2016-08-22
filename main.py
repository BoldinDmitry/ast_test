import functions_ast
import codegen
import time
import ast

code = """
a = 10
b = 20
"""

print(functions_ast.get_variables(code))
