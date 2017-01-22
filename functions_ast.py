import random
import string
import ast
import codegen


def list_generator(__code):
    """
    Создает случаный набор переменных/чисел для list
    :param __code: код, из которого нужно взять перменные
    :return:
    """
    variables = get_variables(__code, True)
    list_len = random.randint(1, 10)
    for_return = []
    if variables:
        for d in range(list_len):
            num_for_list = random.choice([variables[random.randint(0, len(variables) - 1)],
                                          random.randint(-100, 100), term_rand(get_variables(code))])
            for_return.append(num_for_list)
    else:
        for k in range(list_len):
            num_for_list = random.choice(random.randint(-100, 100), term_rand(get_variables(code)))
            for_return.append(num_for_list)
    for_return = list(set(for_return))
    if for_return and for_return is not None:
        return for_return
    else:
        list_generator(__code)


def add_list(__code):
    """
    Функция добавляет в код список
    :param __code: код, в который нужно добавить список
    :return: строку с возвращением списка
    """
    list_ast = ast.Assign(targets=[ast.Name(id=random.choice(string.ascii_lowercase))])
    list_nums = list_generator(__code)
    list_ast.value = ast.List(elts=[ast.parse(str(list_nums[0])).body[0].value])
    for i in range(1, len(list_nums) - 1):
        list_ast.value.elts.append(ast.parse(str(list_nums[i])).body[0].value)
    return codegen.to_source(list_ast)


def for_all_vars(line):
    """

    :param line: строка из которой нужно получить имя перменной
    :return: возвращает имя перменной из строки
    """
    variables_names = []
    type_line = type(line.targets[0])
    if type_line == ast.Name:
        variables_names.append(line.targets[0].id)
    elif type_line == ast.Tuple:
        var_num = len(line.targets[0].elts)
        for d in range(var_num):
            variables_names.append(line.targets[0].elts[d].id)
    return variables_names


def get_variables(__code, get_variables_names=False):
    """

    :param get_variables_names: Флаг, указывающий на то, что нужно вернуть только имена перменных
    :param __code: код программы, откуда нужно получить перменные
    :return: возвращает все перменные из кода
    """
    variables_names = []
    for_return = []
    code_ast = ast.parse(__code)
    code_len = len(code_ast.body)
    for i in range(code_len):
        line = code_ast.body[i]

        if type(line) == ast.Assign:
            if type(line.value) == ast.List:
                variables_names += for_all_vars(line)
            else:
                variables_names += for_all_vars(line)

        if type(line) == ast.If:
            for d in range(len(line.body)):
                line_in_if = line.body[d]
                variables_names += for_all_vars(line_in_if)
    if get_variables_names is False:
        try:
            exec(__code)
        except:
            return "Error"

        for i in range(len(variables_names)):
            for_return.append(variables_names[i] + "=" + str(locals()[variables_names[i]]))
        return list(set(for_return))
    else:
        return variables_names


def random_for_logical_term(variables, code):
    random_var = random.choice(variables)
    if type(random_var) == str:
        random_var = random_var.split("=")[0]
    random_term = term_rand(variables, True)

    if type(random_term) == float:
        random_term = int(random_term)
    return random.choice([random_var, best_for_print(code), random_term,
                          random.randint(-100, 100)])


def logical_term(__code, term_count=None):
    """

    :param __code: код той программы, для которой нужно сгенерировать выражение
    :param term_count: необязательный параметр, генерация определнного колличества членов логического выражения
    :return: логическое выражение для переданного кода
    """
    term_operators = [" < ", " > ", " == ", " != "]
    logical_operators = [" or ", " and "]
    variables = get_variables(__code)

    if term_count is None:
        term_count = random.randint(1, 3)

    if len(variables) > term_count * 2:
        variables = variables[0: term_count * 2]

    elif not variables or len(variables) < term_count * 2:
        for d in range(term_count * 2):
            variables.append(str(random.randint(-100, 100)))
    terms = []

    for d in range(term_count):
        term = str(random_for_logical_term(variables, __code)) + str(random.choice(term_operators)) + \
               str(random_for_logical_term(variables, __code))
        if term not in terms:
            terms.append(term)

    for_return = ""
    terms = list(set(terms))

    for d in range(len(terms)):
        for_return += terms[d] + random.choice(logical_operators)
        if d + 1 == len(terms):
            for_return += terms[d]
    return for_return


def add_if(__code):
    """

    :param __code: код, куда надо добавить if
    :return: возвращает if с сгенерированным выражением
    """
    ast_of_if = ast.If(test=ast.parse(logical_term(__code)).body[0].value,
                       body=[], orelse=[])

    return codegen.to_source(ast_of_if)


def add_while(__code):
    """

    :param __code: код, куда нужно добавить while
    :return: возвращает while с сгенерированным выражением
    """
    ast_while = ast.While(test=ast.parse(logical_term(__code)).body[0].value,
                          body=[], orelse=[])
    return codegen.to_source(ast_while)


def term_for_variable(value, term):
    """
    :param value: название переменной
    :param term: число, или выражение для объявления переменной
    :return: код присваивания
    """
    return str(value) + " " + "=" + " " + str(term)


def term_rand(all_variables=None, without_var=False):
    """

    :param without_var: возвращать простое выражение(true), по умолчанию возвращать присвоение пременной
    :param all_variables: лист переменных типа str вида ["a=1", "b=3"](необязательно)
    :return: сгенерированное выражение
    """
    if all_variables is None:
        all_variables = []
    while len(all_variables) >= 2:
        all_variables.pop()

    number_of_numbers = random.randint(len(all_variables) + 1, 4)

    operations_for_generation = ["+", "-", "*", "/"]
    result = 1.0
    while True:
        term = []
        for i in range(number_of_numbers):
            if len(all_variables) - 1 >= i:
                term.append(all_variables[i].split("=")[0])
            else:
                term.append(str(random.randint(1, 20)))

            function = random.choice(operations_for_generation)
            term.append(function)
        if term:

            term.pop(len(term) - 1)
            term_str = " ".join(term)
            term_for_print = term_str
            for i in range(0, len(all_variables) * 2, 2):

                if i != 0:

                    term[i] = all_variables[int(i / 2)].split("=")[1]
                else:

                    term[0] = all_variables[0].split("=")[1]

            term_str = " ".join(term)
            try:
                result = eval(term_str)
            except:
                pass
            if type(result) is not float and -100 < result < 100:
                result = term_for_print
                break
            break
    if without_var:
        return result
    else:
        return term_for_variable(random.choice(string.ascii_lowercase), result) + "\n"


def best_for_print(code):
    """
    :param code: код, который нужно проанализировать
    :return: возвращает переменную, с которой производилось наибольшее колличество действий
    """
    names_of_variables = []
    lines_of_code = code.split("\n")
    for i in range(len(lines_of_code)):
        if "=" in lines_of_code[i]:
            names_of_variables.append(lines_of_code[i].split("=")[0].replace(" ", ""))
    if len(names_of_variables) > 0:
        return max(set(names_of_variables), key=names_of_variables.count)


def print_in_code(__code):
    var_name = best_for_print(__code)
    return "print(" + str(var_name) + ")"

