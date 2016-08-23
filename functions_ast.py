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
    :return: объект AST c печатью строки, или строки, или числа
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


# Функция генерации объявления переменных:
# На вход: название переменной(value), число, или выражение для объявления переменной
# Возвращает: код присваивания в формате string

def term_for_variable(value, term):
    """
    :param value: название переменной
    :param term: число, или выражение для объявления переменной
    :return: код присваивания
    """
    return parse(str(value) + " " + "=" + " " + str(term))


# Функция генерации случайных выражений:
# На вход: лист переменных типа int вида ["a=1", "b=3"](необязательно)
# Возвращает: сгенерированное выражение

def term_rand(all_variables=[]):
    if all_variables:
        number_of_numbers = random.randint(len(all_variables), 5)  # генерация числа колличества действий

    else:
        number_of_numbers = random.randint(1, 5)  # генерация числа колличества действий
    operations_for_generation = ["+", "-", "*", "/"]
    result = 1.0  # объявление переменной типа float

    while True:
        term = []  # переменная для хранения выражения
        for i in range(number_of_numbers):  # наполнение term случайно сгенерированным выражением
            if len(all_variables) - 1 >= i:
                term.append(all_variables[i].split("=")[0])  # Запись в term значение переменной(из all_variables)

            else:
                term.append(str(random.choice(
                    [random.randint(1, 20), random.randint(-10, -1)])))  # Запись в term значение случайного числа

            function = random.choice(operations_for_generation)
            term.append(function)
        if term:

            term.pop(len(term) - 1)  # удаление последнего элемента, так как он не число
            term_str = " ".join(term)
            term_for_print = term_str
            for i in range(0, len(all_variables) * 2, 2):

                if i != 0:  # Замена переменных их значениями в выражении

                    term[i] = all_variables[int(i / 2)].split("=")[1]
                else:

                    pass

            term_str = " ".join(term)
            result = eval(term_str)

            if type(result) is not float and -100 < result < 100:
                result = term_for_print
                break  # Завершение цикла в случае не дробного result
    return result


def get_variables(code):
    """
    Получение переменных из кода
    :param code: код в формате string
    :return: словарь {переменная: значение}(пример: {'a': '10', 'b': '0'})
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
