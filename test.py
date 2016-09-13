from main import generation

from functions_ast import *


def fitness(code_list):
    code_dict = {}
    for i in range(len(code_list)):
        code_dict[random.randint(0, 100)] = code_list[i]
    return code_dict
code_l = []
for i in range(100):
    code_l.append(generation())


code_l_dict = fitness(code_l)
code_l_keys = code_l_dict.keys()
print(random.randint(len(code_l_keys)-3, len(code_l_keys)))
print(fitness(code_l))