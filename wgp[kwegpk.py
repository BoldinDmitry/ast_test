import pickle
import random
from ast import *
import astunparse

operations = ["Add()", "Sub()", "Mult()", "Div()"]

ast_examples = {
    "=": "Assign(targets=[Name(id='variable', ctx=Store())], value=Num(n=number))",

    "+=": "AugAssign(target=Name(id='variable', ctx=Store()), op=operation, value=Num(n=number))",

    "+": "Assign(targets=[Name(id='variable', ctx=Store())], value=BinOp(left=Name(id='variable_left', ctx=Load()), op=operation, right=Name(id='variable_right', ctx=Load())))"
}
with open('ast.pickle', 'wb') as f:
    pickle.dump(ast_examples, f)

with open('ast.pickle', 'rb') as f:
    ast_examples = pickle.load(f)


def variables(variable_name, number):
    return ast_examples["="].replace("variable", variable_name).replace("number", str(number))


def variables_plus(variable_name, operation, number):
    return ast_examples["+="].replace("variable", variable_name, ).replace("operation", operation).replace("number",
                                                                                                           number)


tree = variables("a", 10)
# tree_1 = variables_plus("a", random.choice(operations), random.randint(0, 100))

tree_ast = parse(tree)
tree_ast = fix_missing_locations(tree_ast)


code_from_ast = astunparse.unparse(tree_ast)

print(code_from_ast)
print(exec(code_from_ast))

