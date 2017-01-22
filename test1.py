from functions_ast import *


def parse_print(__code, line_num=None):
    if line_num is not None:
        print(ast.dump(ast.parse(__code).body[line_num]))
    else:
        print(ast.dump(ast.parse(__code)))


