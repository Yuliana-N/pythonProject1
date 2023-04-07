# Создать матрицу случайных чисел и сохранить ее в json файл.

from random import randint
import json


def main():
    n = 5
    matrix = [[randint(0, 10) for j in range(n)] for i in range(n)]
    with open('task_10_07.json', 'w') as json_file:
        data = json.dumps({'matrix': matrix})
        json_file.write(data)


if __name__ == '__main__':
    main()