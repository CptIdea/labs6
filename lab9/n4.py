import io
import PySimpleGUI as sg


def getPretty(students):
    return '\n'.join([x[0] + ' - ' + '   '.join(x[1]) for x in students.items()])


def getStudent(students):
    n = askAnything('Номер студента')

    layout = [
        [sg.Text(f"#{n}")],
        [sg.Text("ФИО:"), sg.Text(students[n][0])],
        [sg.Text("Возраст:"), sg.Text(students[n][1]), sg.Text("Группа:"),
         sg.Text(students[n][2])],
        [sg.Button('OK')]
    ]

    ans_window = sg.Window(layout=layout, title='Посмотри!')
    while True:
        event, values = ans_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад' or event == 'OK':
            ans_window.close()
            return


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
        [sg.Button("Посмотреть всех")],
        [sg.Text("*здесь появится ответ*", key='ans', size=(70, 0))],
        [sg.Button("Посмотреть кого-нибудь", key='add')]
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
            getStudent(students)
        nom_window['ans'].update(f'{getPretty(students)}')
