"""Игра "угадай число"
Компьютер сам загадывает, и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # устанавливаем значения по умолчанию
    count = 0
    range_min = 1
    range_max = 101

    # открываем цикл в котором будем пытаться угадать число в заданном диапазоне
    while True:
        count += 1
        predict_number = np.random.randint(range_min, range_max)  # предполагаемое число
        
        # если предполагаемое число больше загаданного числа, то устанавливаем новую верхнюю границу
        if predict_number > number:
            range_max = predict_number
    
        # если предполагаемое число меньше загаданного числа, то устанавливаем новую нижнюю границу
        elif predict_number < number:
            range_min = predict_number

        # выход из цикла если угадали
        else:
            break  
    return count


def score_game(game_core_v3) -> int:
    
    """За какое количство попыток в среднем за 1000 подходов угадывает число наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)