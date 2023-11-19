import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Используем алгорит бинарного поиска, чтобы угадать число
    count = 0
    range_search = list(range(1, 101))
    low_value = 1
    hight_value = len(range_search)
    while low_value <= hight_value:
        midl_value = int((low_value + hight_value) / 2)
        guess = range_search[midl_value]
        if guess == number:
            break
        if guess > number:
            count += 1
            hight_value = midl_value - 1
        else:
            count += 1
            low_value = midl_value + 1
    # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

print(score_game(game_core_v3))