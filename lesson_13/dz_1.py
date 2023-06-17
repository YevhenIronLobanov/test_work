import random
from random_words import RandomWords
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





