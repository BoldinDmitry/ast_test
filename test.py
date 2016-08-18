from ast import *
import codegen
import random


def variable(name, number):
    return Assign(targets=[Name(id=name, ctx=Store())], value=Num(n=number))


def operations(operation, number_one, number_two):
    return Expr(value=BinOp(left=Num(n=number_one), op=operation, right=Num(number_two)))


def print_ast():
    return Expr(
        value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[], starargs=None,
                   kwargs=None))


term_for_variable = lambda value, term: str(value) + " " + "=" + " " + term
