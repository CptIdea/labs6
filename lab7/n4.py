import csv

students = {}


def execute():
    if len(students) == 0:
        f = open('lab7/students.csv', encoding='UTF-8')
        reader = csv.reader(f, delimiter=';')
        for x in reader:
            if x[0] == '№':
                continue
            students[x[0]] = x[1:]
    answer = students.items()
    text = ''
    for x in answer:
        text += ' '.join(x[1]) + '\n'
    return text


def plus1():
    for x in students:
        students[x][1] = str(int(students[x][1]) + 1)


def saveToFile():
    f = open('lab7/students.csv', encoding='UTF-8',mode='w',newline= '\n')
    writer = csv.writer(f,delimiter=';')
    readyList = [[x[0]]+x[1] for x in students.items()]
    writer.writerows(readyList)


import PySimpleGUI as sg


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("Вывод")],
        [sg.Text("*Здесь появится список студентов", key='ans', size=(0, 20))],
        [sg.Button("Прибавить годик")],
        [sg.Button("Сохранить в файл")]
    ]
    nom_window = sg.Window(title="NomSelector3000", layout=layout)
    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        if event == 'Прибавить годик':
            plus1()
        if event == "Сохранить в файл":
            saveToFile()
        nom_window['ans'].update(f'{execute()}')
