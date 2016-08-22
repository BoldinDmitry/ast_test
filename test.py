import ast
import string

import codegen

from functions_ast import *

code = ""

code += codegen.to_source(
    term_for_variable(random.choice(string.ascii_letters), random.randint(1, 30))) + "\n"
code += codegen.to_source(
    term_for_variable(random.choice(string.ascii_letters), random.randint(1, 30))) + "\n"
lines_number = input()
for i in range(int(lines_number)):
    function_for_line = random.choice([print_ast(random.choice(get_variables(code)).split("=")[0]),
                                       term_for_variable(
                                           random.choice(string.ascii_letters), term_rand())])
    try:
        code += codegen.to_source(function_for_line) + "\n"
    except:
        print(1)
        print(ast.dump(function_for_line))
print(code)
