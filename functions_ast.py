import random
from ast import *

import codegen

variable = lambda name, number: Assign(targets=[Name(id=name, ctx=Store())],
                                       value=Num(n=number))

operations = lambda operation, number_one, number_two: \
    Expr(value=BinOp(left=Num(n=number_one), op=operation, right=Num(number_two)))

print_ast = lambda: Expr(
    value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[], starargs=None,
               kwargs=None))

term_for_variable = lambda value, term: str(value) + " " + "=" + " " + term

operations_ex = [Add(), Sub(), Mult(), Div()]

i = int(input("Введите колличество строчек: \n"))
new_code = ""
old_code = ""



for i in range(i):
    one_line = random.choice([variable("a", random.randint(-20, 20)),
                             operations(random.choice(operations_ex), random.choice(["a", random.randint(-20, 20)]),
                                        random.choice(["a", random.randint(-20, 20)]))])
    new_code += codegen.to_source(one_line) + '\n'
    try:
        exec(new_code)
        old_code = new_code
    except:
        i -= 1
        new_code = old_code

print(new_code)
