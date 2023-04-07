from random import randint


#Написать функцию, которая получает на вход имя и выводит строку вида: “Hello, {name}”. Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
def my_func(name):
   print(f'Hello, {name}')
   return

# Написать программу для работы с матрицами:
# Создание
def func_create_matrix(a,b,n,m):
    matrix_a = []
    for i in range(0, n):
        line = []
        for j in range(0, m):
            line.append(randint(a, b))
        matrix_a.append(line)
    return matrix_a
def func_create_matrix_2(a,b,n,m):
    matrix_b = [[randint(a, b) for j in range(n)] for i in range(m)]
    return matrix_b

# Вывод
def print_matrix(matrix):
    print('Matrix:')
    for i in matrix:
        print(i)
