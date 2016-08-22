import time
import main


def fitness(code):
    try:
        time_start = time.time()
        exec(code)
        time_end = time.time()
    except:
        return 140

    return time_end - time_start


def code_generation():
    big_list = []

    for g in range(1000):
        big_list.append(main.code_generation())
    return big_list


list_of_code = code_generation()
scores = {}
for i in range(len(list_of_code)):
    score = fitness(list_of_code[i])
    scores[score] = list_of_code[i]
scores_from_dic = scores.keys()
scores_from_dic = list(scores_from_dic)
scores_from_dic.sort()
last_scores = []
for i in range(len(scores_from_dic)):
    last_scores.append(scores[scores_from_dic[i]])

print(last_scores[0])
