import math
from time import clock

from functions_ast import *


class CodeGenerator:
    def check_var_size(self, __code, score):
        variables = get_variables(__code)
        if variables == "Error":
            return -10000000000000
        for i in range(len(variables)):
            variable = int(variables[i].split("=")[1])
            score += 20 - math.fabs(variable)
        return score

    def fitness(self, code):
        score = 0
        score = self.check_var_size(self, code, score)
        return score

    def random_line(self, code):
        if code == "":
            return term_rand()
        all_functions = [add_if(code), term_rand(get_variables(code), False),
                         add_while(code), add_for(code)]
        for_return = random.choice(all_functions)
        return for_return

    def new_generation(self, code):
        codes = []
        for i in range(25):
            codes.append(code)
        if not code:
            for i in range(25):
                codes.append(term_rand())
        else:
            len_code = len(codes)
            d = 0
            while d < len_code:
                random_line_for_code = self.random_line(self, codes[d])
                if random_line_for_code != "Error":
                    codes[d] += random_line_for_code
                    d += 1
                else:
                    codes.pop(d)
                    len_code -= 1
                    d += 1
        code_score = {}
        for i in range(len(codes)):
            code_score[self.fitness(self, codes[i])] = codes[i]

        best_code = code_score[max(code_score.keys())]
        return best_code


CodeGen = CodeGenerator
t = clock()
code = CodeGen.new_generation(CodeGen, "")

for i in range(4):
    code = CodeGen.new_generation(CodeGen, code)
print(">>>" + str(clock()-t))
print(code)
