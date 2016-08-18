import random


def term_res(all_result):
    print(all_result)
    number_of_numbers = random.randint(2, 4)
    operations = ["+", "-", "*", "/"]
    term = []
    result = 0

    for i in range(number_of_numbers):
        number = (random.randrange(-20, 20))
        term.append(str(number))
        function = random.choice(operations)
        term.append(function)
    term.pop(len(term) - 1)
    term.insert(0, str(result))
    term.insert(1, "-")
    term = " ".join(term)
    exec(str("result = " + term))
    print(all_result)
    return term


print(term_res(random.randint(-100, 100)))
