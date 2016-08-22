import ast
import string

import codegen

from functions_ast import *


def code_generation():
    code = ""

    code += codegen.to_source(
        term_for_variable(random.choice(string.ascii_letters), random.randint(1, 30))) + "\n"
    code += codegen.to_source(
        term_for_variable(random.choice(string.ascii_letters), random.randint(1, 30))) + "\n"
    for n in range(10):
        function_for_line = random.choice([print_ast(random.choice(get_variables(code)).split("=")[0]),
                                           term_for_variable(
                                               random.choice(string.ascii_letters), term_rand())])
        try:
            code += codegen.to_source(function_for_line) + "\n"
        except:
            print(ast.dump(function_for_line))

    return code

big_list = []

for i in range(1000):
    big_list.append(code_generation())
    print(i)
print(code_generation())
