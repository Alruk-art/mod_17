print('Сортировка пополам')
L = [2, 3, 1, 8, 6, 5, 9, 4, 7]

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину =
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть 2.3.1.4
        right = merge_sort(L[middle:])  # и правую 6,5,9,8,7
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        print (left[i], right[j])
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    print (result)
    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
print(merge_sort(L))

print(' Быстрая сортировка')
def qsort(array, left, right):
    middle = (left+right) // 2

    p = array[middle]
    print (p, array)
    i,j = left, right
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

array = [2, 3, 1, 8, 6, 5, 9, 4, 7]

print (qsort(array, 0, 8))
print (array)

print(' Быстрая случайная сортировка')
import random

def qsort_random(array, left, right):
    p = (random.choice(array[left: right]))
    print (p, array, left, right)
    i,j = left, right
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
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

array = [2, 3, 1, 8, 6, 5, 9, 4, 7]

print (qsort_random(array, 0, 8))
print (array)