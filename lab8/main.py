import PySimpleGUI as sg
from lab8 import select


def window():
    sg.theme('LightGray1')
    furore = ("furore", 18)

    layout = [
        [sg.Text("Выбор задания:")],
        [sg.Button(f'{i}', size=(6, 3)) for i in range(1, 3)],
        [sg.Button(f'{i}', size=(6, 3)) for i in range(3, 5)]
    ]

    lab_window = sg.Window(title="NomSelector3000", layout=layout, font=furore)
    while True:
        event, values = lab_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        lab_window.hide()
        select.selectNom(event)
        lab_window.un_hide()

    lab_window.close()