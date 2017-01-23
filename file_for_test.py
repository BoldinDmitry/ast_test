from functions_ast import *


def parse_print(__code, line_num=None):
    if line_num is not None:
        print(ast.dump(ast.parse(__code).body[line_num]))
    else:
        print(ast.dump(ast.parse(__code)))


code = """
a = 1
for i in range(10):
    print(1)
if a == 2/2:
    print(a)"""


def branching_line(__code, adding_line_str):
    """
    добавление строки в тело циклов/ветвлений
    :param __code: код, куда нужно добавить строку
    :param adding_line_str: строка, которую нужно добавить
    :return:
    """
    __code = ast.parse(__code)
    for i in range(len(__code.body)):
        if type(__code.body[i]) in [ast.For, ast.If, ast.While]:
            __code.body[i].body.append(ast.parse(adding_line_str))
            return codegen.to_source(__code)

