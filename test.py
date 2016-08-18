from ast import *
import codegen
import random


def term_res(result):
    number_of_numbers = random.randint(2, 4)
    print(number_of_numbers)
    operations = ["+", "-", "*", "/"]
    term = []
    for i in range(number_of_numbers):
        number = random.randrange(-20, 20)
        term.append(str(number))
        function = random.choice(operations)
        term.append(function)

    term.pop(len(term) - 1)

    term.insert(0, str(result))
    term.insert(1, "-")
    term = " ".join(term)
    print(result)
    compile(str("result = " + term))
    print(result)

print(term_res(random.randint(-100, 100)))
