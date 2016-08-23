import ast
import string

import codegen

from functions_ast import *


def code_generation():
    code = ""

    code += codegen.to_source(
        term_for_variable(random.choice(string.ascii_letters).lower(), random.randint(1, 30))) + "\n"
    code += codegen.to_source(
        term_for_variable(random.choice(string.ascii_letters).lower(), random.randint(1, 30))) + "\n"
    for n in range(7):
        function_for_line = term_for_variable(random.choice(string.ascii_letters).lower(), term_rand())
        try:
            code += codegen.to_source(function_for_line) + "\n"
        except:
            print("ERROR")
    code += codegen.to_source(print_ast(random.choice(get_variables(code)).split("=")[0])) + "\n    "

    return code


big_list = []

print(code_generation())
