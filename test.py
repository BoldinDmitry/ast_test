import random


def term_rand(all_variables=[]):
    if all_variables:
        number_of_numbers = random.randint(len(all_variables), 5)  # генерация числа колличества действий
    else:
        number_of_numbers = random.randint(2, 5)  # генерация числа колличества действий
    operations_for_generation = ["+", "-", "*", "/"]
    result = 1.0  # объявление переменной типа float
    while True:
        term = []  # переменная для хранения выражения
        for i in range(number_of_numbers):  # наполнение term случайно сгенерированным выражением
            if len(all_variables) - 1 >= i:
                term.append(all_variables[i].split("=")[0])
            else:
                term.append(str(random.randint(-5, 20)))

            function = random.choice(operations_for_generation)
            term.append(function)
        if term:
            term.pop(len(term) - 1)  # удаление последнего элемента, так как он не число
            term_str = " ".join(term)
            term_for_print = term_str
            for i in range(0, len(all_variables)*2, 2):
                print(i)
                if i != 0:
                    term[i] = all_variables[int(i/2)].split("=")[1]
                else:
                    term[i] = all_variables[0].split("=")[1]

            term_str = " ".join(term)
            result = eval(term_str)

            if type(result) is not float and -100 < result < 100:
                result = term_for_print

                break  # Завершение цикла в случае не дробного result
    return result


print(term_rand())
