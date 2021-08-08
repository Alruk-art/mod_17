import math
import random
#from randmun import randint # модуль, с помощью которого перемешиваем массив
print('Сортировка в лоб')
# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 7, 8]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счётчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем, отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
print(count)
print ('Число цифр в числе факториал 100')
fack = str(math.factorial(100))
print (len(fack))

print('Сортировка в макисмум')
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        print (array[i], array[idx_min])
        array[i], array[idx_min] = array[idx_min], array[i]
print(array, count)

print('Сортировка в минимум')
for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        count += 1
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]
print(array, count)

print('Сортировка мой вариант классический, пузырьковый ')
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
print(array, count)


print('Метод вставки разборка')
array = [2, 3, 1, 7]
count = 0
for i in range(1, len(array)):
    s = array[i] # сохраняем для обмена
    idx = i # 1 2 3 4 5 6 7 8
    print(s, array)
    while idx > 0 and array[idx-1] > s:
        array[idx] = array[idx-1] # перемещение вправо
        print(s, array, '*')
        count += 1;
        idx -= 1
    array[idx] = s # затираем. Влево уже проверено там нет больших чисел
print(array, count)

print('Метод вставки 17_8_4 ')
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count += 1;
    array[idx] = x
print (array, count)