import PySimpleGUI as sg


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