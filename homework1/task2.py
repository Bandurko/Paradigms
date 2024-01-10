"""Задача №2
Дан список целых чисел numbers. Необходимо написать в ДЕКЛАРАТИВНОМ стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки."""

from random import randint

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    nums = [randint(-100, 100) for i in range(8)]
    print(nums)
    print(sort_list_declarative(nums))