# import random
# from random_words import RandomWords
# int_list = []
# float_list = []
# str_list = []
# words = RandomWords()
# for i in range(0, 5000):
#     int_list.append(random.randint(0, 1000))
#     float_list.append(random.uniform(0.1, 100.0))
#     str_list.append(words.random_word())
#
# print('Список цілих чисел:', int_list)
# print('Список чисел з плавуючою крапкою:', float_list)
# print('Список слів:', str_list)
# # Створюємо функцію бульбашкового сортування для чисел
# def bubble_sort(data):
#     length = len(data)
#     #Запускаємо цикл
#     for iIndex in range(length):
#         swapped = False
#         for jIndex in range(0, length -iIndex -1):
#             #Запускаємо сортування
#             if data[jIndex] > data[jIndex + 1]:
#                 data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
#                 swapped = True
#         if not swapped:
#             break
import random
from random_words import RandomWords
import time

int_list = []
float_list = []
str_list = []
words = RandomWords()
for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(words.random_word())

print('Список цілих чисел:', int_list)
print('Список чисел з плавуючою крапкою:', float_list)
print('Список слів:', str_list)

# Створюємо функцію бульбашкового сортування для чисел
def bubble_sort(data):
    length = len(data)
    # Запускаємо цикл
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            # Запускаємо сортування
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break

def calculate_average_sort_time(data, iterations):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        bubble_sort(data)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / iterations
    return average_time

iterations = 10
average_time = calculate_average_sort_time(int_list, iterations)
print(f'Середній час сортування цілих чисел: {average_time:.6f} сек.')

average_time = calculate_average_sort_time(float_list, iterations)
print(f'Середній час сортування чисел з плаваючою крапкою: {average_time:.6f} сек.')

average_time = calculate_average_sort_time(str_list, iterations)
print(f'Середній час сортування списку слів: {average_time:.6f} сек.')
