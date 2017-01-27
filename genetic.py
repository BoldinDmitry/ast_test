from functions_ast import *


class CodeGenerator:
    def main(self, __code=""):
        __genetic = Genetic
        code_list = []
        __best_code = []
        for k in range(5):
            for i in range(10):
                print(">>>" + str(k) + " " + str(i))
                __line_of_code = ""
                if __line_of_code != "Error":
                    __code += __line_of_code
                    code_list.append(__code)
            __best_code.append(__genetic.main(__genetic, code_list))

        return random.choice(__best_code)

    def random_line(self, __code):
        if __code == "":
            return term_rand()
        variables = get_variables(__code)
        if variables == "Error":
            return variables
        all_functions = [term_rand(variables), print_in_code(__code),
                         add_if(__code), add_for(__code), add_while(__code)]  # массив из функций
        line_of_code = random.choice(all_functions)
        print(line_of_code)
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


code_gen = CodeGenerator

print(code_gen.main(code_gen))

