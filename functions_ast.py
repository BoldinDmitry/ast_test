import random
from ast import *
import codegen


def term_res(result):
    result_res = result
    number_of_numbers = random.randint(2, 4)
    print(number_of_numbers)
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
    # print(term, result)
    term.insert(0, str(result))
    term.insert(1, "-")
    term = " ".join(term)
    # print(term)
    exec(str("result = " + term))
    return term





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
