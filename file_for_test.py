from functions_ast import *


def parse_print(__code, line_num=None):
    if line_num is not None:
        print(ast.dump(ast.parse(__code).body[line_num]))
    else:
        print(ast.dump(ast.parse(__code)))


code = """
for i in range(10):
    print(1)"""

parse_print(code, 0)



