from functions_ast import *


def parse_print(__code, line_num=None):
    if line_num is not None:
        print(ast.dump(ast.parse(__code).body[line_num]))
    else:
        print(ast.dump(ast.parse(__code)))


code = """
for i in range(10):
    print(1)"""

parse_print(code, 0)


def add_for(code):
    arguments_score = random.randint(1, 3)
    if arguments_score == 1:
        ast.For(target=ast.Name(id=random.choice(string.ascii_lowercase), ctx=ast.Store()),
                iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()),
                args=[ast.Num(n=random.randint(0, 100))], keywords=[], starargs=None, kwargs=None))
    elif arguments_score == 2:
        ast.For(target=ast.Name(id=random.choice(string.ascii_lowercase), ctx=ast.Store()),
                iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()),
                args=[ast.Num(n=random.randint(0, 100)), ast.Num(n=random.randint(0, 100))],
                              keywords=[], starargs=None, kwargs=None))
