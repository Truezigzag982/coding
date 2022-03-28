import PySimpleGUI as sg

sg.theme('BluePurple')
layout = [
    [sg.Text('Theme to choose :) \/ \/')],
    [sg.Text('choose a theme, to see what is it like', size=(25, 2))],
    [sg.Listbox(values = sg.theme_list(), size=(20, 12),
                key='-LIST-', enable_events=True)],
    [sg.Button('Exit')]
]

window = sg.Window('Theme example', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    theme = values['-LIST-'][0]
    sg.theme(theme)
    sg.popup_get_text(f'theme you choose: {theme}')


window.close()