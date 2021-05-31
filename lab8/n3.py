import csv
import io

import PySimpleGUI as sg

rawList = [
    ['1', 'Иванов Иван Иванович', '13', 'ВКБ11'],
    ['2', 'Петрова Петр Петрович', '15', 'ВКБ12'],
    ['3', 'Семенов Семен Семенович', '22', 'ВКБ13']
]


def reloadStudents(students):
    ans = {rawList[i][0]: rawList[i][1:] for i in range(len(rawList))}
    students.clear()
    students.update(ans)


def routeEvent(event, students):
    if event == 1:
        printSpecialStudents(students, lambda x: x[2] == 'ВКБ11')
    elif event == 2:
        printSpecialStudents(students, None, [f'{i}' for i in range(1, 10)])
    elif event == 3:
        printSpecialStudents(students, lambda x: x[1] == '22')
    elif event == 4:
        printSpecialStudents(students, lambda x: x[0].split()[0] == 'Иванов')
    elif event == 5:
        printSpecialStudents(students, lambda x: x[0].split()[0][-1] == 'а')
    elif event == 6:
        printSpecialStudents(students, lambda x: int(x[1]) % 2 == 0)
    elif event == 7:
        printSpecialStudents(students, lambda x: '5' in x[1])
    elif event == 8:
        printSpecialStudents(students, lambda x: len(x[2]) > 7)
    elif event == 9:
        printSpecialStudents(students, None, [f'{i}' for i in students.keys() if int(i) % 2 == 0])
    elif event == 10:
        printSpecialStudents(students, None, [f'{i}' for i in students.keys() if i[-1] == '1'])


def printStudents(students):
    string = io.StringIO()
    print(students, file=string)
    return string.getvalue()


def findBy(condition, students):
    ans = []
    for k in students:
        if condition(students[k]):
            ans += k
    return ans


def printSpecialStudents(students, condition, keys=None):
    if keys is None:
        keys = []
        keys = findBy(condition, students)

    ans = {x: students[x] for x in keys if students.get(x) is not None}
    students.clear()
    students.update(ans)


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("Вывод")],
        [sg.Text("*Здесь появится список студентов*", key='ans', size=(0, 20))],
        [sg.Button('Студентов группы "БО - 111111".', key=1)],
        [sg.Button('Студентов с номерами 1-10.', key=2)],
        [sg.Button('Студентов в возрасте 22 лет.', key=3)],
        [sg.Button('Студентов с фамилией "Иванов".', key=4)],
        [sg.Button('Студентов, чьи фамилии заканчиваются на «а».', key=5)],
        [sg.Button('Студентов, чей возраст – четное число.', key=6)],
        [sg.Button('Студентов, если в возрасте студента встречается число 5.', key=7)],
        [sg.Button('Студентов, если их номера группы длиннее 7 символов.', key=8)],
        [sg.Button('Студентов, если их «№» четное число.', key=9)],
        [sg.Button('Студентов, если их номер группы заканчивается на «1».', key=10)],
    ]
    nom_window = sg.Window(title="NomSelector3000", layout=layout)

    students = {rawList[i][0]: rawList[i][1:] for i in range(len(rawList))}

    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        reloadStudents(students)
        if type(event) == int:
            routeEvent(event, students)
        nom_window['ans'].update(f'{printStudents(students)}')
