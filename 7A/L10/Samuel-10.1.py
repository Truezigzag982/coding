import PySimpleGUI as sg


layout = [
    [sg.Text('pls enter your name: ')],
    [sg.Text('Name: '), sg.Input()],
    [sg.Button('Finish!'), sg.Button('Exit!')]
]

window = sg.Window('Name \/ \/', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit!':
        break

    if event == 'Finish!':
        print('Hello: ', values[0])
        print('Event: ', event)

window.close()