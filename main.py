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

    if key == "types_play":
        line_gen("str", all_variables)


def code_analyze():
    all_variables.extend(get_variables(code_for_variables))
    lines_from_code = code.split("\n")

    if len(lines_from_code) >= 5:
        random.choice([expression_generation("types_play", all_variables),
                       expression_generation("term_gen", all_variables)])

    if len(lines_from_code) < 1:
        expression_generation("create_var")

    if 5 >= len(lines_from_code) >= 1 and len(all_variables) <= 3:
        random.choice([expression_generation("create_var", all_variables),
                       expression_generation("term_gen", all_variables)])


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



while len(code.split("\n")) <= 7:
    code_analyze()

code += "print(" + best_for_print(code) + ")"

print(code)
ant = input("Будет ли ошибка в коде?")
try:
    exec(code)
    if ant == "не будет":
        print("Всё правильно")
    else:
        print("ERROR")
except:
    if ant != "не будет":
        print("Всё правильно")
    else:
        print("ERROR")
