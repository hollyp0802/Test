import PySimpleGUI as sg

menu_layout = [['File', ['Open', 'Exit']], ['Help', ['About']]]
my_layout = [
    [
        sg.Text("Something about this window"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(200, 100), key="-FILE LIST-"
        )
    ],
]

layout = [
    [   sg.Menu(menu_layout),
        sg.Column(my_layout),
    ]
]

window = sg.Window("Testing", layout, size=(1000, 500), resizable=True)
# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
              
window.close()
