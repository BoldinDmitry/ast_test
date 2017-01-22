import ast
import astor


# subscript
code_sub = ast.Subscript(ast.Name("x", ast.Store()), ast.Index(ast.Num(3)), ast.Load())

# unary
code_unary = ast.UnaryOp(ast.Not(), ast.Name("x", ast.Store()))

# bool
code_bool = ast.BoolOp(ast.And(), [code_unary, code_sub])

# retrun
code_return = ast.Return(ast.Name("x", ast.Store()))

# if
code_if = ast.If(code_bool, [ast.Pass()], [code_return])

# var1 += var2
code_var_sum = ast.AugAssign(ast.Name("s", ast.Store()), ast.Add(), ast.Name("x", ast.Store()))

# for
x = ast.Name("x", ast.Store())
y = ast.Name("y", ast.Load())
e = ast.Return("s")
code_for = ast.For(x, y, [code_var_sum], [e])

# while
code_while = ast.While(ast.Num(3), [code_var_sum], [])

# function
a = ast.arguments([], None, [], [], None, [])
code_function = ast.FunctionDef("x", a, [code_if, code_for, code_while, code_return], [], None)


if __name__ == '__main__':
    vars = dict(globals())
    code = [vars[c] for c in sorted(list(vars)) if c.startswith('code_')]

    for c in code:
        print("{sep}\n\n{obj}\n\n{code}\n".format(
            sep="-="*42, obj=c, code=astor.to_source(c)
        ))