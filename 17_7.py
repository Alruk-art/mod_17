def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

#array = list(map(int, input().split()))
#print (array)
#element = int(input())

#print(find(array, element))

def cnt(num):
    nn.count(num)
    print (nn.count(num), end = ' = ')
    if nn.count(num):
        return True
    return False
print ("Число вхождений в массив")
nn = [1, 2, 3, 4, 6, 6, 11, 22]
num = 6
print (nn, 'числа ', num)
print (cnt(num))

print ('Из курса')
def cnt(nn, num):
    cnt = 0
    for a in nn:
        if a == num:
            cnt += 1
    return cnt

print (cnt(nn, num))


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search (array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search (array, element, middle + 1, right)





def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search (array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search (array, element, middle + 1, right)

array = [i for i in range (1, 10, 2)]  # 1,2,3,4,...
print ('index = ', array)
element = int (input( "element <10 = " ))

# запускаем алгоритм на левой и правой границе
print (binary_search (array, element, 0, 9))