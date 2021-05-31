import io
import PySimpleGUI as sg


def execute(rawList):
    out = {rawList[i][0]: rawList[i][1:] for i in range(len(rawList))}
    print(out)

    string = io.StringIO()
    print(out, file=string)
    return string.getvalue()


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Button("execute!")],
        [sg.Text("*здесь появится ответ*", key='ans', size=(70, 0))]
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)

    rawList = [
        ['1', 'ФИО', 'Возраст', 'Группа'],
        ['2', 'ФИО', 'Возраст', 'Группа'],
        ['3', 'ФИО', 'Возраст', 'Группа']
    ]

    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        nom_window['ans'].update(f'{execute(rawList)}')
