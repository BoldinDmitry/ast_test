import random
from functions_ast import *


def expression_generation(key, all_variables=None):
    if all_variables is None:
        all_variables = []
    if key == "create_var":
        expression_for_line, expression_var = term_rand(all_variables)
        print(expression_for_line)

    if key == "term_gen":
        key = random.choice(["create_var", "old_var"])

        if key == "create_var":
            expression_for_line, expression_var = term_rand(all_variables)
            print(expression_for_line, key)

        if key == "old_var":
            expression_for_line, expression_var = term_rand(all_variables)
            print(expression_for_line, key)

    if key == "old_var":
        expression_for_line, expression_var = term_rand(all_variables)
        print(expression_for_line)


expression_generation("term_gen")
