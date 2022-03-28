import PySimpleGUI as sg


layout = [
    [sg.Text('pls enter the name of a plant that you like: ')],
    [sg.Text('Plant name: '), sg.Input(do_not_clear=False, key='_NAME_')],
    [sg.Text('', key='_OUTPUT_')],
    [sg.Button('Finish!'), sg.Button('Exit!')]
]

window = sg.Window('Plants \/ \/', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit!':
        break

    if event == 'Finish!':
        message = 'The plant you like is: ', values['_NAME_']
        window.Element('_OUTPUT_'). Update(message)

window.close()
