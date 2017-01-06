from functions_ast import *


class Code_generator:
    def main(self):
        __genetic = Genetic
        code_list = []
        code = ""
        for k in range(5):
            for i in range(100):
                __line_of_code = ""
                __line_of_code += self.random_line(__line_of_code) + "\n"
                code_list.append(__line_of_code)
            __best_code = __genetic.main(__genetic, code_list)
            code += __best_code
        return code

    def random_line(self, __code):
        all_functions = ["a = 1 + 4 * 2", print_in_code(__code)]  # массив из функций
        line_of_code = random.choice(all_functions)
        return line_of_code


class Genetic:
    def main(self, list_of_code):
        code_with_score = {}
        for i in range(len(list_of_code)):
            score = self.fitness(self, list_of_code[i])
            code_with_score[score] = list_of_code[i]
        scores = code_with_score.keys()
        best = code_with_score[max(scores)]
        return best

    dict_of_tasks = {}

    def fitness(self, __code):
        score = 0
        list_of_lines = __code.split("\n")
        for i in range(len(list_of_lines)):
            score += self._get_probability(self, i, list_of_lines[i])
        return score + random.randint(0, 900)

    def _get_probability(self, number_of_line, line_of_code):
        return random.randint(0, 100)

code_gen = Code_generator

print(Code_generator.random_line(code_gen, "a=10"))