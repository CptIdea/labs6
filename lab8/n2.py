import builtins
import io

import PySimpleGUI as sg


def routeEvent(event, students):
    if event == 1:
        condAsk = askAnything("ФИО")
        changeValue(lambda x: [x[0], str(int(x[1]) + 1)] + x[2:], students, lambda x: x[0] == condAsk)
    elif event == 2:
        condAsk = askAnything("ФИО")
        changeValue(lambda x: [askAnything("Новое ФИО")] + x[1:], students, lambda x: x[0] == condAsk)
    elif event == 3:
        changeValue(lambda x: [x[0], str(int(x[1]) + 1)] + x[2:], students, askAnything("Номер студента"))
    elif event == 4:
        condAsk = askAnything("ФИО")
        changeValue(lambda x: x[:2] + [askAnything("Новая группа")], students, lambda x: x[0] == condAsk)
    elif event == 5:
        changeValue(lambda x: None, students, askAnything("Номер студента"))
    elif event == 6:
        changeValue(lambda x: [x[0], str(int(x[1]) - 1)] + x[2:], students, lambda x: int(x[1]) > 22)
    elif event == 7:
        changeValue(lambda x: None, students, lambda x: int(x[1]) == 23)
    elif event == 8:
        changeValue(lambda x: [x[0], str(int(x[1]) + 1)] + x[2:], students, lambda x: x[0].split()[0] == 'Иванов')
    elif event == 9:
        changeValue(lambda x: ['Сидоров ' + ' '.join(x[0].split()[1:])] + x[1:], students,
                    lambda x: x[0].split()[0] == 'Иванов')
    elif event == 10:
        changeValue(lambda x: [x[2], x[1], x[0]], students, None)


def askAnything(thing):
    sg.theme('LightGray1')
    furore = ("furore", 18)

    layout = [
        [sg.Text(f'Введите {thing}')],
        [sg.Input(key="ans")],
        [sg.Button("OK")]
    ]

    window = sg.Window('LabController3000', layout, font=furore)
    ans = ''

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        ans = ''
    ans = values['ans']

    window.close()
    return ans


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


def changeValue(changer, students, condition):
    if str(type(condition)) == "<class 'function'>":
        keys = findBy(condition, students)
        for k in keys:
            students[k] = changer(students[k])
    elif type(condition) == str:
        students[condition] = changer(students[condition])
    else:
        for k in students:
            students[k] = changer(students[k])


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("execute!")],
        [sg.Text("*здесь появится ответ*", key='ans', size=(70, 0))],
        [sg.Button(
            'Увеличить возраст конкретного студента на 1. Поиск по «ФИО» («ФИО» студента необходимо ввести с клавиатуры).',
            key=1)],
        [sg.Button(
            'Изменить «ФИО» студента. Поиск по «ФИО» (старое и новое «ФИО» студента необходимо ввести с клавиатуры).',
            key=2)],
        [sg.Button(
            'Увеличить возраст конкретного студента на 1. Поиск по «№» («№» студента необходимо ввести с клавиатуры).',
            key=3)],
        [sg.Button(
            'Изменить группу студента. Поиск по «ФИО» («ФИО» студента и новый номер группы необходимо ввести с клавиатуры).',
            key=4)],
        [sg.Button(
            'Удалить запись о студенте. Поиск по «№» («№» студента, которого нужно удалить из списка, задается с клавиатуры)',
            key=5)],
        [sg.Button('Если возраст студента больше 22 уменьшить его на 1.', key=6)],
        [sg.Button('Если возраст студента равен 23, удалить его из списка.', key=7)],
        [sg.Button('У всех студентов с фамилией «Иванов» увеличить возраст на 1.', key=8)],
        [sg.Button('У студентов с фамилией «Иванов» изменить фамилию на «Сидоров».', key=9)],
        [sg.Button('Поменять «ФИО» и «Группа» местами.', key=10, metadata=10)],
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)

    rawList = [
        ['1', 'Иванов Иван Иванович', '13', 'ВКБ11'],
        ['2', 'Петров Петр Петрович', '15', 'ВКБ12'],
        ['3', 'Семенов Семен Семенович', '19', 'ВКБ13']
    ]
    students = {rawList[i][0]: rawList[i][1:] for i in range(len(rawList))}

    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        if type(event) == int:
            routeEvent(event, students)
        nom_window['ans'].update(f'{printStudents(students)}')
