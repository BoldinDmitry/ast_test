import string
from functions_ast import *
import codegen

"""
Ключи к expr_gen:
create_var - создать переменную (первый if)
term_gen - сгенерировать случайное выражение (второй if)
new_var - действие создание новой переменной
old_var - переделование одной из старый переменных
print_var - печать переменной
types_play - изменение типов переменных
"""

all_variables = []
code = ""
code_for_variables = ""


def what_to_print():
    name_var_for_print = random.choice([all_variables])
    line_of_code = print_ast(name_var_for_print)
    return line_of_code


def expression_generation(key, all_variables=None):
    if all_variables is None:
        all_variables = []
    if key == "create_var":
        expression_for_line, expression_var = term_rand(all_variables)
        line_gen(key, expression_for_line, expression_var)

    if key == "term_gen":
        key = random.choice(["create_var", "old_var"])

        if key == "create_var":
            expression_for_line, expression_var = term_rand(all_variables)
            line_gen(key, expression_for_line, expression_var)

        if key == "old_var":
            expression_for_line, expression_var = term_rand(all_variables)
            line_gen(key, expression_for_line, expression_var)

    if key == "old_var":
        expression_for_line, expression_var = term_rand(all_variables)
        line_gen(key, expression_for_line, expression_var)


def code_analyze():
    if len(code.split("\n")) >= 1:
        random.choice([expression_generation("term_gen", all_variables),
                       expression_generation("create_var", all_variables)])
    else:
        expression_generation("create_var", all_variables)


def line_gen(key, expression=None, expression_var=None):
    global code
    global code_for_variables
    line_of_code = ""

    if key == "create_var":
        variable_name = random.choice(string.ascii_letters).lower()
        line_of_code = variable_name + " = " + expression
        code_for_variables = variable_name + " = " + str(eval(expression_var)) + "\n"
    if key == "old_var":
        all_variables = get_variables(code_for_variables)
        variable_name = random.choice(all_variables).split("=")[0]

        for k in range(len(all_variables)):
            all_variables[k] = all_variables[k].split("=")[0]
        line_of_code = variable_name + " = " + expression
        code_for_variables += variable_name + " = " + str(eval(expression_var)) + "\n"

    if key == "str":
        variable_name = random.choice(expression).split("=")[0]
        line_of_code = variable_name + " = str(" + variable_name + ")"
        code += line_of_code + "\n"
        line_of_code = "print(type(" + variable_name + "))"

    if line_of_code != "":
        code += line_of_code + "\n"


def generation():
    try:
        while len(code.split("\n")) <= 4:
            code_analyze()
    except:
        generation()
    return code
