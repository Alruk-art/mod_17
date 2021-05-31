# Практическая работа  17_9_1

def list_numb():
    while True:
        l_n = input('Введите несколько целых чисел через пробел: ')
        try:
            l_n = list(map(int, l_n.split()))
            if len(l_n) == 1:
                print('список короткий')
                raise ValueError
        except ValueError:
            print("Неверный формат данных")
        else:
            break
    return l_n
def ch_num():
    while True:
        ch_num = input('ведите любое целое число: ')
        try:
            value = int(ch_num)
            break
        except ValueError as e:
            print(f'Значение {ch_num} содержит недопустимые символы')
    return ch_num

def metod():
    while True:
        ms = input ("1- метод быстрой сортировки, 0 - метод сортировки вставками ")
        try:
            ms = int(ms)
            if ms == 1 or ms == 0:
                break
            print ("Не выбран метод")
        except ValueError as e:
            print("Выберите метод сортировки 1 или 0")
    return ms
# метод сортировки вставками
def list_sort(l_n):
    for i in range(1, len(l_n)):
        x = l_n[i]
        idx = i
        while idx > 0 and l_n[idx - 1] > x:
            l_n[idx] = l_n[idx - 1]
            idx -= 1
        l_n[idx] = x
    return l_n

 # метод быстрой сортировки
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array

# двоичный поиск
def binary_search(array, element, left, right):
    #if left > right:  # если левая граница превысила правую,
    #    return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search (array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search (array, element, middle + 1, right)


l_n = list_numb() # Начало. ввод списка и контрольного числа
c_n = ch_num() # новый элемент
l_n.append(int(c_n)) # добавляем новый элемент в список
ms = metod()
if ms == 2:
    list_sort(l_n) # сортируем вставками
    print (f"после сортировки вставками, {l_n}")
else:
    array = l_n
    left = 0
    right = len(array)-1
    print ('Быстрая сортировка')
    l_n = qsort(array, left ,right) # быстрая сортировка
    print (f"после быстрой сортировки, {array}")

array = l_n # готовим значения для поиска
element = int(c_n) # ищем его место в  списке
left = 0
right = len(l_n)-1

ind = binary_search (array, element, left, right) # вызов двоичного поиска

print ('Поиск индекса элемента в списке')
for i in range(len(array)):
    print (f'{i+1}:{array[i]}, ', end="")
print ()
# print (ind)
if ind == 0 or ind == 1 and array[ind-1] == array[ind]: # в случае если первое число совпадает с новым
    print ('Это первый элемент в списке')
elif ind == (len(array)-1):
    print('Это последний элемент в списке')
else:
    print ("индекс ", ind+1, ", после ", array[ind-1], end="")
    if array[ind] == array[ind + 1]:
        print(', следующее число в списке совпадает с добавленным')
    else:
        print (" перед ", array[ind+1])

# 31/05/2011
