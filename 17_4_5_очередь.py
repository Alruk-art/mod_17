N_max = int(input("Определите размер очереди:(3,4,5)"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0

def size(): # получаем размер очереди
    if is_empty(): # если она пуста
        return 0 # возвращаем ноль
    elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
        return N_max # значит очередь заполнена
    elif head > tail: # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else: # или если хвост стоит правее начала
        return tail - head


def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max

def do():
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0  # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max  # и циклично перемещаем указатель



def show():
    print("Задача №%d в приоритете" % (queue[head]))
    print ('Количество задач', order, 'Вся очередь', N_max)

def exit():
    return 0

while True:
    cmd = input("Введите команду:check, size, add, show, do, exit: ")
    if cmd == "check":
        if is_empty():
            print("Очередь пустая1")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая2")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая3")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")