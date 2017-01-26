from functions_ast import *


def parse_print(__code, line_num=None):
    if line_num is not None:
        print(ast.dump(ast.parse(__code).body[line_num]))
    else:
        print(ast.dump(ast.parse(__code)))


lines_count = 10
code = ""
code += term_rand()
all_functions = [add_if(code), term_rand(get_variables(code), False), add_while(code), add_for(code)]

for i in range(5):
    code += random.choice(all_functions)
code += print_in_code(code)
print(code)
