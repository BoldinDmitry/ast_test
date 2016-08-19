import random


# функция генерации случайных выражений:

def term_res():
    number_of_numbers = random.randint(3, 5)  # генерация числа колличества действий
    operations = ["+", "-", "*", "/"]
    result = 1.0  # объявление переменной типа float

    while True:
        term = []  # переменная для хранения выражения
        for i in range(number_of_numbers):  # наполнение term случайно сгенерированным выражением
            number = random.randrange(1, 20)
            term.append(str(number))
            function = random.choice(operations)
            term.append(function)

        term.pop(len(term) - 1) # удаление последнего элемента, так как он не число
        term_str = " ".join(term)
        result = eval(term_str)

        if type(result) is not float and result < 100 and result > -100 and term:
            print(term)
            result = [term_str, result]
            break  # Завершение цикла в случае не пустого term, не дробного result

    return result


print(term_res())
