import random
from ast import *


def variable(name, number):
    return Assign(targets=[Name(id=name, ctx=Store())], value=Num(n=number))


def operations(operation, number_one, number_two):
    return Expr(value=BinOp(left=Num(n=number_one), op=operation, right=Num(number_two)))


def print_ast():
    return Expr(
        value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[], starargs=None,
                   kwargs=None))


def term_for_variable(value, term):
    return str(value) + " " + "=" + " " + term


def term_res(result):
    number_of_numbers = random.randint(2, 4)
    print(number_of_numbers)
    operations = ["+", "-", "*", "/"]
    term = []
    result = 0
    for i in range(number_of_numbers):
        number = (random.randrange(-20, 20))
        term.append(str(number))
        function = random.choice(operations)
        term.append(function)
    term.pop(len(term) - 1)
    term.insert(0, str(result))
    term.insert(1, "-")
    term = " ".join(term)
    exec(str("result = " + term))
    return term


operations_ex = [Add(), Sub(), Mult(), Div()]
