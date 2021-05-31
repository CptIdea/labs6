def execute():
    print("test")


import PySimpleGUI as sg


def window():
    sg.theme('LightGray1')

    layout = [
        [sg.Text("lab example")]
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)
    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        nom_window['ans'].update(f'{execute()}')
