'''
Корреляция
 Контекст
Корреляция - статистическая мера, используемая для оценки
связи между двумя случайными величинами.
 Ваша задача
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.
'''

import math


def correlation(arr_1, arr_2):

    if len(arr_1) != len(arr_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(arr_1)

    mean_x = sum(arr_1) / n
    mean_y = sum(arr_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in arr_1]) / len(arr_1)
    variance_y = sum([(yi - mean_y) ** 2 for yi in arr_2]) / len(arr_2)

    numerator = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(arr_1, arr_2)]) / len(arr_1)
    denominator = math.sqrt(variance_x * variance_y)

    if denominator == 0:
        return 0

    return numerator / denominator


data_1 = [1, 2, 3, 4, 5]
data_2 = [2, 3, 600, 8, 10]

print(f"Корреляция Пирсона: {correlation(data_1, data_2)}")
