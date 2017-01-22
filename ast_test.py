import ast
import codegen

__code = """
hui, dermo = 10, 20
a = 1
print(hui)
if a == 1:
    a = 0
    c = 1
b = 2 * 4 * hui"""


def for_all_vars(line):
    variables_names = []
    type_line = type(line.targets[0])
    if type_line == ast.Name:
        variables_names.append(line.targets[0].id)
    elif type_line == ast.Tuple:
        var_num = len(line.targets[0].elts)
        for d in range(var_num):
            variables_names.append(line.targets[0].elts[d].id)
    return variables_names


def all_vars(code):
    variables_names = []
    for_return = []
    code_ast = ast.parse(code)
    code_len = len(code_ast.body)
    for i in range(code_len):
        line = code_ast.body[i]
        if type(line) == ast.Assign:
            variables_names += for_all_vars(line)
        if type(line) == ast.If:
            for d in range(len(line.body)):
                line_in_if = line.body[d]
                variables_names += for_all_vars(line_in_if)
    try:
        exec(__code)
    except:
        return "Error"

    for i in range(len(variables_names)):
        for_return.append(variables_names[i] + "=" + str(locals()[variables_names[i]]))
    return list(set(for_return))


print(all_vars(__code))
