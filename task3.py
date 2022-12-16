# Задайте список из n чисел 
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Enter number: ')) 

def Sequence(n):
    my_list = []
    for i in range(1, n+1):
        my_list.append(round((1 + 1 / i)**i, 2))
    return my_list 
        
print(Sequence(n))
print(sum(Sequence(n)))