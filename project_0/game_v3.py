import numpy as np

def binary_search_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0  # счетчик попыток
    low = 1  # нижняя граница поиска
    high = 100  # верхняя граница поиска

    while low <= high:
        count += 1
        mid = (low + high) // 2  # середина диапазона
        if mid < number:
            low = mid + 1  # сдвигаем нижнюю границу выше середины
        elif mid > number:
            high = mid - 1  # сдвигаем верхнюю границу ниже середины
        else:
            return count  # если угадали, возвращаем количество попыток

def score_game(predict_function) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        predict_function (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для хранения количества попыток
    np.random.seed(1)  # фиксируем seed для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # генерируем массив случайных чисел

    for number in random_array:
        count_ls.append(predict_function(number))  # применяем функцию угадывания к каждому числу

    score = int(np.mean(count_ls))  # вычисляем среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__ == '__main__':
    score_game(binary_search_predict)  # запускаем оценку игры
