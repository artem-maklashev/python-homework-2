# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не число. Повторите ввод ")
    return number

def Factorial(number):
    if number == 1:
        return  1  
    else:
        return number*Factorial(number-1)

def GetMatrix(number):
    my_lyst = []
    for i in range(number):
        print(Factorial(i+1))
        my_lyst.append(Factorial(i+1))
    return my_lyst

number = GetNumber('Введите число ')
matrix = GetMatrix(number)
print(f'N = {number} -> {matrix}')



