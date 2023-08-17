import random


def is_valid(number):
    """ Проверка числа на уникальность. Все 4 цифры числа должны быть разные """
    try:
    # переводим наше число в список из символов.
    # сравниваем с множеством.
    # (в множестве нет повторяющихся символов)
        number_list = list(str(number))
        if len(set(number_list)) == 3:
            return True
        return False
    except:
        return False
# переменные
number_guess = 0  # загаданное число
number_computer = 0  # число, которое нужно отгадать
n = 0  # кол-во попыток
# списки
n_c = []
n_b = []
# генерируем число, которое нужно отгадать
while not is_valid(number_guess):
    number_guess = random.randint(100, 999)
# генерируем число от которого наша программа будет отталкиваться
while not is_valid(number_computer):
    number_computer = random.randint(100, 999)


def check(number_guess, number_computer):
    """ Находим количество коров и быков в числе """

    # индексы коров и быков
    n_c, n_b = [], []

    try:
        # переводим наши числа в список из символов.
        number_guess_list = list(str(number_guess))
        number_computer_list = list(str(number_computer))

        # проходимся по числ
        for index in range(len(number_guess_list)):

            # если в разных числа в одинаковых
            # индексах цифры ровны,   то это бык
            if number_computer_list[index] == number_guess_list[index]:
                n_b.append(index)
            # если в числах есть одинаковые цифры, но на разных местах, то это корова
            elif number_guess_list[index] in number_computer_list:
                n_c.append(index)

        # возвращаем списки индексов коров и быков
        return n_c, n_b

    except:
        return n_c, n_b


def game(number_guess, n_c, n_b):
    """ Ф-я, пересоборки числа из имеющихся данных """

    # переводим наше число в список из символов
    number_guess_list = list(str(number_guess))

    # проходимся по списку number_guess_list
    for index in range(len(number_guess_list)):
        # если индекса цифры нет в списке индексов быков,
        # но есть в в списке коров
        if index not in n_b and index in n_c:
            # рандомным способом переставляем
            index_random = n_c[random.randint(0, len(n_c)-1)]
            number_guess_list[index], number_guess_list[index_random] = number_guess_list[index_random], number_guess_list[index]
        # если индекса цифры нет ни в одном из списков
        if index not in n_b and index not in n_c:
            number_guess_list[index] = str(random.randint(0, 9))
            while not is_valid(int(''.join(number_guess_list))):
                number_guess_list[index] = str(random.randint(0, 9))

    return int(''.join(number_guess_list))


# главный цикл, работает, пока не будет 4 быка, то есть
# два числа не будут ровны между собой

# получаем списки индексов коров и быков
n_c, n_b = check(number_guess, number_computer)

while len(n_b) != 3:
    # пересоберем число из имеющихся данных
    number_guess = game(number_guess, n_c, n_b)

    # получаем списки индексов коров и быков
    n_c, n_b = check(number_guess, number_computer)
    n += 1
    print(f"Попытка: {n}; Число: {number_guess}; Число, которое нужно отгадать: {number_computer}")

print(number_guess)