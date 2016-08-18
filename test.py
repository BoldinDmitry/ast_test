import random
from ast import *


def term_res(result):
    result_res = result
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
    # print(term, result)
    term.insert(0, str(result))
    term.insert(1, "-")
    term = " ".join(term)
    # print(term)
    exec(str("result = " + term))

    if str(result * 1000)[len(result)-1] != "0":
        term_res(result_res)
    else:
        print(result)

term_res(random.randint(20, 20))