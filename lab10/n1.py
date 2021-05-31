import io
import PySimpleGUI as sg
from lab10 import asker

rawMatrix = """1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2
1 3 5 7 9 7 5 3
3 1 5 3 2 6 5 7
1 7 5 9 7 3 1 5
2 6 3 5 1 7 3 2"""


def getPretty(matrix):
    return '\n'.join(
        ['   '.join(
            [str(y) for y in x]
        )
            for x in matrix]
    )


def newMatrix():
    return [[int(n) for n in m.split()] for m in rawMatrix.split('\n')]


def toZero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = 0


def toN(matrix):
    m = int(asker.askAnything('m'))
    n = int(asker.askAnything('n'))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < m:
                matrix[i][j] = n


def toTwentyFive(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 5:
                matrix[i][j] = matrix[i][j] * matrix[i][j]


def toSmaller(matrix):
    l = len(matrix)
    while 0 < l - 4 < len(matrix):
        del matrix[-1]


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("Вывод", key='reload')],
        [sg.Text("*здесь появится матрица*", key='ans', size=(25, 10))],
        [sg.Button("Заменить четные на 0", key='to_zero')],
        [sg.Button("Заменить <m на n", key='to_n')],
        [sg.Button("Все пятерки в квадрат", key='to_twenty_five')],
        [sg.Button("Удалить последние 4 строки", key='to_smaller')],
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)
    matrix = newMatrix()
    print(matrix)

    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break

        if event == 'to_zero':
            toZero(matrix)
        if event == 'to_n':
            toN(matrix)
        if event == 'to_twenty_five':
            toTwentyFive(matrix)
        if event == 'to_smaller':
            toSmaller(matrix)

        if event == 'reload':
            matrix = newMatrix()

        nom_window['reload'].update('Новая матрица')
        nom_window['ans'].update(f'{getPretty(matrix)}')
