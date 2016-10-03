from functions_ast import *

code = """a = 1
b = 5
"""


class Make_Task:
    def make_error(self, key, __code):
        pass

    def make_answer(self, key, __code):
        pass


make_task = Make_Task()
print(make_task.make_error(random.choice(["name_error", "division_by_zero"]), code))


class Code:
    ast_of_code = dump(code)

    def to_string(self):
        pass


class code_generator:
    def random_line(self):
        pass

    genetic


class genetic:
    dict_of_tasks = {}

    def fitness_function(self):
        score = random.randint(0, 100)
        return score

    def get_probability(self):
        pass