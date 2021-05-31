import PySimpleGUI as sg
from select import selectLab

sg.theme('LightGray1')
furore = ("furore", 18)

layout = [
    [sg.Text("Выбор лабы:")],
    [sg.Button(f'{i}', size=(6, 3)) for i in range(7, 10)],
    [sg.Button(f'{i}', size=(6, 3)) for i in range(10, 13)]
]

window = sg.Window('LabController3000', layout, font=furore)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        print("Спасибо за использование LabController3000. На ваше имя выписан счёт за использование")
        break
    window.hide()
    selectLab(event)
    window.un_hide()

window.close()