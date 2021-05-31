import io
import PySimpleGUI as sg


def getPretty(students):
    return '\n'.join([x[0] + ' - ' + '   '.join(x[1]) for x in students.items()])


def removeStudent(students):
    n = askAnything('Номер студента')
    students.__delitem__(n)


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


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("Вывод")],
        [sg.Text("*здесь появится ответ*", key='ans', size=(70, 0))],
        [sg.Button("Удалить кого-нибудь", key='add')]
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)
    students = {
        '1': ['Иванов Иван Иванович', '23', 'ВКБ22'],
        '2': ['Петров Петр Петрович', '23', 'ВКБ23'],
        '3': ['Семенов Семен Семенович', '23', 'ВКБ21']
    }

    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        if event == 'add':
            removeStudent(students)
        nom_window['ans'].update(f'{getPretty(students)}')


def do_something():
    pass
