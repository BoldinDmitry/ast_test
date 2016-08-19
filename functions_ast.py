import random
from ast import *


# Присвоение переменной определенное значение:
# На вход: переменная(name) и значение переменной(number)
# На выход: объект AST с объявлением переменной

def variable(name, number):
    return Assign(targets=[Name(id=name, ctx=Store())], value=Num(n=number))


# Выполнение математический операций:
# На вход: название операции(operation), левое число(number_one), правое число(number_two)
# На выход: объект AST с объявлением переменной

def operations(operation, number_one, number_two):
    return Expr(value=BinOp(left=Num(n=number_one), op=operation, right=Num(number_two)))


def print_ast():
    return Expr(
        value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[], starargs=None,
                   kwargs=None))


# Функция генерации объявления переменных:
# На вход: название переменной(value), число, или выражение для объявления переменной
# На выход: код присваивания в формате string

def term_for_variable(value, term):
    return str(value) + " " + "=" + " " + term


# Функция генерации случайных выражений:
# На вход: ничего не требует
# На выход: лист, состоящий из сгенерированного выражения(result[0]) и значения сгенерированого выражения(result[1])

def term_rand():
    number_of_numbers = random.randint(3, 5)  # генерация числа колличества действий
    operations_for_generation = ["+", "-", "*", "/"]
    result = 1.0  # объявление переменной типа float

    while True:
        term = []  # переменная для хранения выражения
        for i in range(number_of_numbers):  # наполнение term случайно сгенерированным выражением
            number = random.randrange(1, 20)
            term.append(str(number))
            function = random.choice(operations_for_generation)
            term.append(function)

        term.pop(len(term) - 1)  # удаление последнего элемента, так как он не число
        term_str = " ".join(term)
        result = eval(term_str)

        if type(result) is not float and -100 < result < 100 and term:
            print(term)
            result = [term_str, result]
            break  # Завершение цикла в случае не пустого term, не дробного result

    return result
