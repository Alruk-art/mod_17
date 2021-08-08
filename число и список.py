def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def find_position(arr, key):
    left = -1
    right = len(arr)
    while right > left + 1:
        mid = (left + right) // 2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid
    return right

raw_string = (11, 66, 33, 44, 55)

list_of_numbers = list(raw_string)
print ('Дан ряд чисел', list_of_numbers)

while True:

    raw_value = input('Введите целое число: ')
    try:
        value = int(raw_value)
        break
    except ValueError as e:
        # print('Ввод %s содержит недопустимые символы' % (raw_value))
        print(f'Ввод {raw_value} содержит недопустимые символы')
sorted_list = sort(list_of_numbers)
print(sorted_list)
if value < sorted_list[0]:
    print('Введенное число меньше всех остальных')
elif value == sorted_list[0]:
    print(f'Введеное число равно самому маленькому элементу в списке')
elif value > sorted_list[-1]:
    print('Введенное число больше всех остальных')
else:
    list_of_numbers.append(value)
    print (list_of_numbers.append(value))
    #sorted_list = sort(list_of_numbers)
    pos = find_position(sorted_list, value)
    print (pos)
    print(f'Индекс элемента меньше чем введеное число - {pos}')