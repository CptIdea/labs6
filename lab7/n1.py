def get_len(slovar):
    return len(slovar)


import PySimpleGUI as sg


def window():
    sg.theme('LightGray1')


    layout = [
        [sg.Text("Словарь: { 1:3,'4':'бла-бла' }."
                 "\n\nПредположительная длина = 2")],
        [sg.Button("execute!")],
        [sg.Text("*здесь появится ответ*", key='ans')]
    ]

    nom_window = sg.Window(title="NomSelector3000", layout=layout)
    while True:
        event, values = nom_window.read()
        if event == sg.WINDOW_CLOSED or event == 'Назад':
            break
        nom_window['ans'].update(f'{get_len({1: 3, "4": "бла-бла"})}')
