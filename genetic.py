import main


def fitness(code):

    score = 40
    try:
        exec(code)
    except:
        score -= 40
    if "=" not in code:
        return 0
    lines_of_code = code.split("\n")
    variables_from_code = ""
    for i in range(len(lines_of_code)):
        if "=" in lines_of_code[i] and lines_of_code[i].split("=")[0].replace(" ", "") not in variables_from_code:
            variables_from_code += lines_of_code[i].split("=")[0].replace(" ", "")
            score -= i
    for i in range(len(lines_of_code)):
        if "print" in lines_of_code[i]:
            score += i

    return score


def code_generation():
    big_list = []

    for g in range(1000):
        big_list.append(main.code_generation())
    return big_list


scores = {}
list_of_code = code_generation()

for i in range(len(list_of_code)):
    score = fitness(list_of_code[i])
    scores[score] = list_of_code[i]
scores_from_dic = scores.keys()
scores_from_dic = list(scores_from_dic)
scores_from_dic.sort()
last_scores = []
for i in range(len(scores_from_dic)):
    last_scores.append(scores[scores_from_dic[i]])

print(last_scores[len(last_scores)-1])
print(last_scores[0])
