import fibo
from naive import naive
import timeit
from RabinKarp import RabinKarp
from BoyerMur import BoyerMeow
from KnutMorrisPratt import KnutMorissPratt

line = fibo.fibonacci(500)

# Наивный
arr = []
#t1 = timeit.default_timer()
for i in range(10, 100):
    arr.append(naive(str(line), str(i)))
#print(timeit.default_timer() - t1)
print(f'Число {arr.index(max(arr)) + 10} встречается {max(arr)} раз')

# Рабина-Карпа
arr = []
# t1 = timeit.default_timer()
for i in range(10, 100):
    arr.append(RabinKarp(str(line), str(i)))
# print(timeit.default_timer() - t1)
print(f'Число {arr.index(max(arr)) + 10} встречается {max(arr)} раз')

# Бойер-Мура
arr = []
# t1 = timeit.default_timer()
for i in range(10, 100):
    arr.append(BoyerMeow(str(line), str(i)))
# print(timeit.default_timer() - t1)
print(f'Число {arr.index(max(arr)) + 10} встречается {max(arr)} раз')

# Кнута-Морриса-Пратта

arr = []
# t1 = timeit.default_timer()
for i in range(10, 100):
    arr.append(KnutMorissPratt(str(line), str(i)))
# print(timeit.default_timer() - t1)
print(f'Число {arr.index(max(arr)) + 10} встречается {max(arr)} раз')