
def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print (n)
print (p(5))

#Задание 17.4.4 с одной скобкой
def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент — открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False
    return len(stack) == 0
# print (par_checker('([5+6])*([7+8])/([4+3])'))

#Задание 17.4.5_1 с ([]) скобками
def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно

        if s == "(" or s == "[":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек

        if  s == "]" or s ==")":
            if len(stack) == 0:
                return False

            if len(stack) > 0:
                stack.pop()

                # если встретилась закрывающая скобка, то проверяем
                # пуст ли стек и является ли верхний элемент — открывающей скобкой
                # удаляем из стека
    return len(stack) == 0

        #if len(stack): # иначе завершаем функцию с False
    #return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False

string='([5+6])*([7+8])/([4+3])'
print (par_checker(string))

#Задание 17.4.5_1 с ([]) скобками через ключи



def w_par_cheker(string):
    stack = []
    d = {'(': ')', '[': ']'} # строго
    k = d.keys()
    v = d.values()
    # print (d.keys())
    # print (d.values())
    # print (d.items())
    string = '([5+6])*([7+8])/([4+3])'
    for s in string:
        if s in k:
            stack.append(s)
            # print ('>', len(stack))
        if s in v:
            if len(stack) == 0:
                return False
            if len(stack) > 0:
                stack.pop()
                # print('<', len(stack))

    # print('=', len(stack))
    return len(stack) == 0

print (w_par_cheker(string))