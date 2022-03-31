import PySimpleGUI as sg

sg.theme('Python')

layout = [[sg.Text('ToDo list ofr this week(check after finish (:  )')]]

for i in range(1, 6):
    layout.append([sg.Text(f'{i}. '), sg.CBox(''), sg.Input()])

layout.append([sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')])

window = sg.Window('Working assistance', layout)
filename = 'todolist.data'

while True:
    event, values = window.read()
    if event in(None, 'Exit'):
        break
    elif event == 'Save':
        window.save_to_disk(filename)
    elif event == 'Load':
        window.load_from_disk(filename)
window.close()