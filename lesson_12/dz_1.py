from multiprocessing import Pool
import threading
import time

# Створюємо функцію для розрахунку факторіала
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Створюємо функцію для обчислення за методом мультипроцессінгу
def calculate_factorial_multiprocessing(numbers):
    with Pool() as pool:
        result = pool.map(factorial, numbers)

    # print('ProcessPoolExecutor result:', result)
    # print('ProcessPoolExecutor time:',  multiprocessing_time)
    return result
# Створюємо функцію для обчислення за допомогою модуля threading
def calculate_factorial_threading(numbers):
    results = []
    # Створюємо функцію розрахунку факторіала і додаємо результати до занального списку результатів
    def calculate(number):
        result = factorial(number)
        results.append(result)

    # Створюємо список, який містить всі потоки обчислення
    threads = []
    for number in numbers:
        thread = threading.Thread(target=calculate, args=(number,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results

if __name__ == '__main__':
    numbers = [5, 7, 3, 4, 6]
    multiprocessing_results = calculate_factorial_multiprocessing(numbers)
    threading_results = calculate_factorial_threading(numbers)

    # print('ThreadPoolExecutor results:', threading_results)

    # start_time = time.time()
    # threading_time = time.time() - start_time
    # print("ThreadPoolExecutor time:", threading_time)

    # Обчислюємо час виконання за допомогою threading
    start_time = time.time()
    threading_time = time.time() - start_time
    # print('ThreadPoolExecutor time:', threading_time)
    # Обчислюємо час виконання за допомогою multiprocessing
    start_time = time.time()
    multiprocessing_time = time.time() - start_time
    # print('ProcessPoolExecutor time:', multiprocessing_time)

    # Порівнюємо швидкість обчислення і виводимо назву оптимального методу
    if multiprocessing_time < threading_time:
        print('Обробка методом ThreadPoolExecutor вища.')
    elif threading_time < multiprocessing_time:
        print('Швідкість обробки методом ProcessPoolExecutor  вища.')
    else:
        print('Швидкість обробки методом ProcessPoolExecutor і ThreadPoolExecutor однакова.')








