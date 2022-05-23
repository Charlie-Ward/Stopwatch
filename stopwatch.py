import PySimpleGUI as sg
from time import time


def create_window():
    sg.theme('black')

    layout = [
        [sg.Push(), sg.Image('cross.png', key='-Close-', enable_events=True, pad=0)],
        [sg.VPush()],
        [sg.Text('', font='Young 60', key="-Time-")],
        [sg.Button("Start", button_color=('#FFFFFF', '#FF0000'), font='Young', border_width=0, key="-StartStop-"),
         sg.Button("Lap", button_color=('#FFFFFF', '#FF0000'), font='Young', border_width=0, key="-Lap-",
                   visible=False)],
        [sg.Column([[]], key = '-Laps-')],
        [sg.VPush()],
    ]

    return sg.Window('Stopwatch', layout, size=(300, 300), no_titlebar=True, element_justification='center')


window = create_window()
start_time = 0
Laps = 0
active = False

while True:
    event, values = window.read(timeout=10)

    if event in (sg.WIN_CLOSED, "-Close-"):
        break

    if event == "-StartStop-":
        if active:
            active = False
            window['-StartStop-'].update('Reset')
            window['-Lap-'].update(visible=False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                Laps = 0
            else:
                start_time = time()
                active = True
                window['-StartStop-'].update('Stop')
                window['-Lap-'].update(visible=True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-Time-'].update(elapsed_time)

    if event == '-Lap-':
        Laps += 1
        window.extend_layout(window['-Laps-'], [[sg.Text(Laps), sg.VSeparator(), sg.Text(elapsed_time)]])

window.close()
