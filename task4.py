# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

import random
def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не число. Повторите ввод ")
    return number

def GetList(number):
    my_list = []
    for i in range(number):
        my_list.append(random.randrange(-number, number+1))
    return my_list

def Multiply(my_list):
    multiply = -1
    file = open('file.txt', 'r')
    first_index = int(file.readline())
    seconsd_index = int(file.readline())
    if first_index > len(my_list) -1 or seconsd_index > len(my_list) -1:
        print("Индексы в файле file.txt за пределами списка")
        
    else:
        print(f'Умножаем элементы с индексами {first_index} и {seconsd_index}')
        multiply = my_list[first_index]*my_list[seconsd_index]
    return multiply

def ShuffleList(my_list):
    for i in range(len(my_list)-1, -1, -1):
        j = random.randint(0, i + 1)
        my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


number = GetNumber('Введите число ')
my_list = GetList(number)
result = Multiply(my_list)
print(f'N = {number} -> {my_list} -> {result}')
shuffle_lyst = ShuffleList(my_list)
print(shuffle_lyst)
        