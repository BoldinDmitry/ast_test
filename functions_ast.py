import random
from ast import *


# Присвоение переменной численное значение:
# На вход: переменная(name) и значение переменной(number)
# Возвращает: объект AST с объявлением переменной

def variable(name, number):
    return Assign(targets=[Name(id=name, ctx=Store())], value=Num(n=number))


# Печать переменных, чисел и строк:
# На вход: название переменной(variable_name), или строка(text_for_print), или число(number_for_print)
# Возвращает: объект AST c печатью строки, или строки, или числа

def print_ast(variable_name=None, string_for_print=None, number_for_print=None):
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
    return parse(str(value) + " " + "=" + " " + str(term))


# Функция генерации случайных выражений:
# На вход: лист переменных типа int вида ["a=1", "b=3"](необязательно)
# Возвращает: сгенерированное выражение

def term_rand(all_variables=[]):
    if all_variables:
        number_of_numbers = random.randint(len(all_variables), 5)  # генерация числа колличества действий

    else:
        number_of_numbers = random.randint(2, 5)  # генерация числа колличества действий
    operations_for_generation = ["+", "-", "*", "/"]
    result = 1.0  # объявление переменной типа float

    while True:
        term = []  # переменная для хранения выражения
        for i in range(number_of_numbers):  # наполнение term случайно сгенерированным выражением
            if len(all_variables) - 1 >= i:
                term.append(all_variables[i].split("=")[0])  # Запись в term значение переменной(из all_variables)

            else:
                term.append(str(random.randint(-5, 20)))  # Запись в term значение случайного числа

            function = random.choice(operations_for_generation)
            term.append(function)
        if term:

            term.pop(len(term) - 1)  # удаление последнего элемента, так как он не число
            term_str = " ".join(term)
            term_for_print = term_str
            for i in range(0, len(all_variables) * 2, 2):

                print(i)
                if i != 0:  # Замена переменных их значениями в выражении

                    term[i] = all_variables[int(i / 2)].split("=")[1]
                else:

                    term[i] = all_variables[0].split("=")[1]

            term_str = " ".join(term)
            result = eval(term_str)

            if type(result) is not float and -100 < result < 100:
                result = term_for_print
                break  # Завершение цикла в случае не дробного result
    return result
