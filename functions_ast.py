import random
from ast import *


def variable(name, number):
    """

    :param name: название переменной
    :param number: значение переменной
    :return: объект AST с объявлением переменной
    """

    return Assign(targets=[Name(id=name, ctx=Store())], value=Num(n=number))


def print_ast(variable_name=None, string_for_print=None, number_for_print=None):
    """

    :param variable_name: название переменной
    :param string_for_print: название строки
    :param number_for_print: число
    :return: объект AST c печатью строки, или числа
    """

    if variable_name:
        return Expr(
            value=Call(func=Name(id='print', ctx=Load()), args=[Name(id=variable_name, ctx=Load())],
                       keywords=[],
                       starargs=None, kwargs=None))

    if number_for_print:
        return Expr(
            value=Call(func=Name(id='print', ctx=Load()), args=[Num(n=number_for_print)], keywords=[], starargs=None,
                       kwargs=None))

    if string_for_print:
        return Expr(
            value=Call(func=Name(id='print', ctx=Load()), args=[Str(s=string_for_print)], keywords=[], starargs=None,
                       kwargs=None))


def term_for_variable(value, term):
    """
    :param value: название переменной
    :param term: число, или выражение для объявления переменной
    :return: код присваивания
    """
    return parse(str(value) + " " + "=" + " " + str(term))


def term_rand(all_variables=None):
    """

    :param all_variables: лист переменных типа str вида ["a=1", "b=3"](необязательно)
    :return: сгенерированное выражение
    """
    if all_variables is None:
        all_variables = []

    while len(all_variables) >= 4:
        all_variables.pop()

    number_of_numbers = random.randint(len(all_variables) + 1, 5)

    operations_for_generation = ["+", "-", "*", "/"]
    result = 1.0
    while True:
        term = []
        for i in range(number_of_numbers):
            if len(all_variables) - 1 >= i:
                term.append(all_variables[i].split("=")[0])

            else:
                term.append(str(random.randint(1, 20)))

            function = random.choice(operations_for_generation)
            term.append(function)
        if term:

            term.pop(len(term) - 1)
            term_str = " ".join(term)
            term_for_print = term_str
            for i in range(0, len(all_variables) * 2, 2):

                if i != 0:

                    term[i] = all_variables[int(i / 2)].split("=")[1]
                else:
                    term[0] = all_variables[0].split("=")[1]

            term_str = " ".join(term)
            try:
                result = eval(term_str)
            except:
                pass
            if type(result) is not float and -100 < result < 100:
                result = term_for_print
                break
    return result, term_str


def get_variables(code):
    """
    Получение переменных из кода
    :param code: код в формате str
    :return: лист переменных типа str вида ["a=1", "b=3"]
    """

    variables = []
    splited_code = str(code).split("\n")
    for i in range(len(splited_code)):

        if splited_code[i].find("=") != -1:
            splited_line = splited_code[i].split("=")

            for n in range(len(splited_line)):
                splited_line[n] = splited_line[n].strip()

            variables.append(splited_line[0] + "=" + splited_line[1])

    return variables


def best_for_print(code):
    """
    :param code: код, который нужно проанализировать
    :return: возвращает переменную, с которой производилось наибольшее колличество действий
    """
    names_of_variables = []
    lines_of_code = code.split("\n")
    for i in range(len(lines_of_code)):
        if "=" in lines_of_code[i]:
            names_of_variables.append(lines_of_code[i].split("=")[0].replace(" ", ""))
    if len(names_of_variables) > 0:
        return max(set(names_of_variables), key=names_of_variables.count)
