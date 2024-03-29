'''
Бинарный поиск
 Контекст
Предположим, что мы хотим найти элемент в массиве (получить его индекс). Мы можем это сделать просто перебрав все
элементы. Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск. Принцип прост:
сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти. Если центральный элемент
больше нашего, рассматриваем массив слева от центрального, а если больше - справа и повторяем так до тех пор, пока не
найдем наш элемент.

 Ваша задача
Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.
'''

from random import randint

'''
Для решения условия задачи (написании блока бинарного поиска) использовалась структурная и процедурная (создание 
функции для повторного использования) парадигмы, являющиеся частями императивной парадгмы.
'''
def binary_search(arr: list[int], n: int):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (end + start) // 2

        if arr[mid] == n:
            return mid

        elif arr[mid] < n:
            start = mid + 1

        elif arr[mid] > n:
            end = mid - 1

    return -1

'''
Для сортировки сгенерированного массива случайных чисел, использовалась функциональная, декларативная парадигма.
'''
if __name__ == '__main__':
    l = int(input("\nВведите размер массива: "))
    unsort_arr = [randint(-100, 100) for i in range(l)]

    print(f'\nСгенерированный неотсортированный массив', unsort_arr)

    sort_arr = sorted(unsort_arr)
    print(f'\nМассив отсортированный по возрастанию', sort_arr, '\n')

    num = int(input("Введите число, индекс которого нужно найти: "))

    if binary_search(sort_arr, num) == -1:
        print('\nТакого числа в данном массиве нет')

    else:
        print(f'\nИндекс числа ', num, ' равен ', binary_search(sort_arr, num))
