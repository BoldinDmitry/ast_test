import random
from ast import *
import codegen


def term_res(result):
    number_of_numbers = random.randint(2, 4)
    operations = ["+", "-", "*", "/"
                                 ""]
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


operations_ex = [Add(), Sub(), Mult(), Div()]

i = int(input("Введите колличество строчек: \n"))
new_code = ""
old_code = ""
n = 0
while n <= i:
    one_line = random.choice([variable("a", random.randint(-20, 20)),
                              operations(random.choice(operations_ex), random.choice(["a", random.randint(-20, 20)]),
                                         random.choice(["a", random.randint(-20, 20)]))])
    new_code += codegen.to_source(one_line) + '\n'
    try:
        exec(new_code)
        old_code = new_code
        n += 1
    except:
        new_code = old_code

print(new_code)
