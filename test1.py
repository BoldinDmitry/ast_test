import ast
import codegen

from functions_ast import *


def random_for_logical_term(variables, code):
    random_var = random.choice(variables)

    if type(random_var) == str:
        random_var = random_var.split("=")[0]

    random_term = term_rand(variables, True)

    if type(random_term) == float:
        random_term = int(random_term)
    return random.choice([random_var, best_for_print(code), random_term,
                          random.randint(-100, 100)])


def logical_term(code, term_count=None):
    term_operators = [" < ", " > ", " == ", " != "]
    logical_operators = [" or ", " and "]
    variables = get_variables(code)
    if not term_count:
        term_count = random.randint(1, 3)
    if len(variables) > term_count * 2:
        variables = variables[0: term_count * 2]
    elif not variables or len(variables) < term_count * 2:
        for d in range(term_count * 2):
            variables.append(str(random.randint(-100, 100)))
    terms = []
    for d in range(term_count):
        term = ""
        term += str(random_for_logical_term(variables, code)) + str(random.choice(term_operators)) + \
                str(random_for_logical_term(variables, code))

        if term not in terms:
            terms.append(term)

    for_return = ""

    for d in range(len(terms)):
        for_return += terms[d] + random.choice(logical_operators)
        if d + 1 == len(terms):
            for_return += terms[d]
    return for_return


def add_if(code):
    """

    :param code: старый код
    :return: код плюс синтаксическая конструкция if с pass внутри
    """
    __code_str = """if 1 == 1:
        pass
    """
    __code_str = ast.parse(__code_str)
    __code_str.body[0].test = ast.parse(logical_term(code)).body[0]
    code += "\n" + codegen.to_source(__code_str)
    return code


print(add_if("a=1"))
