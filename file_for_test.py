from _socket import timeout

import math

from functions_ast import *
from time import clock, time
from pytimeout import *


def parse_print(__code, line_num=None):
    if line_num is not None:
        print(ast.dump(ast.parse(__code).body[line_num]))
    else:
        print(ast.dump(ast.parse(__code)))


def fitness(code):
    score = 0
def check_var_size(code, score):
    variables = get_variables(code)
    for i in range(len(variables)):
        print(variables[i])
        variable = int(variables[i].split("=")[1])
        score += 20 - math.fabs(variable)
    return score

code = """
e = 11 - 6 + 3
j = e + 2
while (j + 7 + 18 == j):
    r = j - 4 * 7 + 10
for j in range(22, 30):
    i = j + 7 + 19
if ((i - 14 - 4 * 5 < i - 7 * 3) or ((i * 19 > i) and (e > i))):
    d = i + 16 + 2 + 5
if (((i == i) and (e > i - 2)) or (i != i)):
    x = i + 6 - 12
for d in range(17, 30):
    u = i - 10 - 1
for v in range(1, 34, 4):
    s = i - 4 + 14 - 20
for v in range(22, 29):
    m = d + 20 + 8 - 13
p = d - 18 * 4
while ((u == d * 15) or (d * 18 * 6 * 2 == d - 3 * 17)):
    q = d - 7 + 4"""

code1 = """
a = 1
b = 2
c = 2*10"""

print(str(fitness(code1)) + " vs " + str(fitness(code)))

