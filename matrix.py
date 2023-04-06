
# Создать  матрицу размерностью n × m элементов и заполнить ее случайными значениями от 1 до 9.
from random import randint
print('Введите диапазон: ')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
print('Введите размер матрицы: ')
n = int(input('Enter n: '))
m = int(input('Enter m: '))
matrix_a = []
for i in range(0, n):
    line = []
    for j in range(0, m):
        line.append(randint(a, b))
    matrix_a.append(line)
    print(line)
# идентично matrix = [ [ random.randint(1, 11) for j in range(n)] for i in range(m) ]


#Создать квадратную матрицу размерностью n и заполнить ее случайными значениями. Найти сумму всех элементов матрицы, которые кратны 3.

sum_ = 0
for i in range(0, n):
    line = []
    for j in range(0, n):
        line.append(randint(1, 9))
        if line[j]%3 == 0:
            sum_+= line[j]
    matrix_a.append(line)
    print(line)
print(sum_)


# Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива.

quantity = 0
for i in matrix_a:
    for j in i:
        if j == 7:
            quantity += 1
print('quantity 7:',quantity)


# Найти максимальный элемент матрицы.

matr_max = matrix_a[0][0]
for t in matrix_a:
    for k in t:
        if matr_max < k:
            matr_max = k
print('Максимальное число: ',matr_max)


# Найти сумму всех элементов матрицы.

elem_summ = 0
for t in matrix_a:
    for k in t:
        elem_summ += k
print('Сумма элементов: ',elem_summ)

# Обнулить все элементы выше главной диагонали.
print(f'9) Matrix by task 9:')
for i in range(0, n):
    for j in range(i + 1, m):
        matrix_a[i][j] = 0
    print(matrix_a[i])

# Обнулить все элементы ниже главной диагонали.

for j in range(0, m):
    for i in range(j + 1, n):
        matrix_a[i][j] = 0

print(f'10) Result matrix')
for line in matrix_a:
    print(line)



# Найти индекс ряда с максимальной суммой элементов.
index_of_max_row = 0
# max_sum = matr_min * n * m
max_sum = 0
for i in range(0, n):
    row_summ = 0
    for j in range(0, m):
        row_summ += matrix_a[i][j]
    if row_summ > max_sum or i == 0:
        index_of_max_row = i
        max_sum = row_summ
print( 'Индекс максимального ряда: ',index_of_max_row, matrix_a[index_of_max_row])



# Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а

fam = ['Палахов', 'Семенов', 'Иванова', 'Петрова']
for i in fam:
    print(i[0])
    print(i[len(i)-1])
    if i[0] == 'П' and i[-1] == 'а': # -1 первый элемент списка с конца
        print(i)

# Дан список слов. Сгенерировать новый список с перевернутыми словами
maf = []
for i in fam:
    print(i[::-1])
    maf.append(i[::-1])
print(maf)
