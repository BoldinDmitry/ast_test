from functions_ast import *

class Make_Task:
    """
    KEYS:
        name_error
        division_by_zero
    """

    def __name_error(self, __code):
        none_var = ""
        all_variables = get_variables(__code)
        variables = []
        for i in range(len(all_variables)):
            variables.append(all_variables[i].split("=")[0])
        while not none_var:
            variable_name = random.choice(string.ascii_lowercase)
            if variable_name not in variables:
                none_var = variable_name

        return term_rand([none_var + "=" + str(random.randint(1, 25))])

    def __division_by_zero(self, __code):
        new_code = ""
        variable_name = random.choice(string.ascii_lowercase)
        new_code += term_for_variable(variable_name, 0) + "\n"
        new_code += term_for_variable(random.choice(string.ascii_lowercase),
                                      str(best_for_print(__code)) + "/" + str(variable_name)) + "\n"
        return new_code

    def division_by_zero_answer(self, __code):
        answers = {}
        right = random.randint(1, 4)
        for i in range(4):
            if right == i:
                try:
                    exec(__code)
                except Exception as e:
                    answers["right"] = str(e)
            else:
                answers[i] = str(random.choice(["name '" + get_variables(code)[
                    random.randint(0, len(get_variables(code))-1)].split("=")[0] + "' is not defined",
                                                "division by zero", "syntax error"]))
        print(answers)

    def name_error_answer(self, __code):
        pass

    def make_error(self, key, __code):
        error_type = {
            "division_by_zero": self.__division_by_zero(__code),
            "name_error": self.__name_error(__code)
        }[key]
        __code += error_type + "\n"
        self.make_answer(key, __code)
        return __code

    def make_answer(self, key, __code):
        answers = {
            "division_by_zero": self.division_by_zero_answer(__code),
            "name_error": self.name_error_answer(__code)
        }[key]
        return __code


make_task = Make_Task()
print(make_task.make_error(random.choice(["name_error", "division_by_zero"]), code))


class Task:
    dict_tasks = {"if": 1, "while": 1, "for": 1, "math": 1}
    def get_probability(self):
        return random.choice(0, 1000) / 1000
