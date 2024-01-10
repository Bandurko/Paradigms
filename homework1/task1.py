"""Задача №1
Дан список целых чисел numbers. Необходимо написать в ИМПЕРАТИВНОМ стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки."""

from random import randint

def sort_list_imperative(numbers):
    if len(numbers) == 1:
        return numbers
    for i in range(len(numbers)):
        for j in range (i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

if __name__ == '__main__':
    nums = [randint(-100, 100) for i in range(8)]
    print(nums)
    print(sort_list_imperative(nums))