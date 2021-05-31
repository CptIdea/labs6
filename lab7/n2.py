import csv
def execute():
    f = open('lab7/students.csv',encoding='UTF-8')
    reader = csv.reader(f,delimiter=';')
    students = {}
    for x in reader:
        if x[0] == '№':
            continue
        students[x[0]] = x[1:]


    answer = students.items()
    list(answer).sort(key=lambda x: x[1][0])
    text = ''
    for x in answer:
        text += ' '.join(x[1])+'\n'

    return text

import PySimpleGUI as sg


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("Вывод")],
        [sg.Text("*Здесь появится список студентов, отсортированых по фамилии",key='ans',size=(0,20))]
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)
    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        nom_window['ans'].update(f'{execute()}')
