from functions import func_create_matrix
from functions import func_create_matrix_2
from functions import print_matrix

def main():
    print('Введите диапазон: ')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print('Введите размер матрицы: ')
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    matrix = func_create_matrix(a, b, n, m)
    print_matrix(matrix)
    matrix_b = func_create_matrix_2(a, b, n, m)
    print_matrix(matrix_b)

if __name__ == '__main__':
   main()

