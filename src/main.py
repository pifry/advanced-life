import PySimpleGUI as sg
import random
import string

sg.theme('DarkAmber')
sg.theme('SystemDefault')

CANVAS_SIZE = (20, 20)
BOX_SIZE = 25

layout = [
    [sg.Text("Multidimensional Conway's Game of Life"), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((CANVAS_SIZE[0]*BOX_SIZE, CANVAS_SIZE[1]*BOX_SIZE), (0, CANVAS_SIZE[1]*BOX_SIZE), (CANVAS_SIZE[0]*BOX_SIZE, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False)],
    [sg.Button('Start'), sg.Button('Exit')]
]

window = sg.Window('Window Title', layout, finalize=True)

g = window['-GRAPH-']

for row in range(CANVAS_SIZE[1]):
    for col in range(CANVAS_SIZE[0]):
        g.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black')


while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    mouse = values['-GRAPH-']

    if event == '-GRAPH-':
        if mouse == (None, None):
            continue
        box_x = mouse[0]//BOX_SIZE
        box_y = mouse[1]//BOX_SIZE
        cell_location = (box_x * BOX_SIZE + 18, box_y * BOX_SIZE + 17)
        print(box_x, box_y)
        g.draw_rectangle((box_x * BOX_SIZE, box_y * BOX_SIZE), (box_x * BOX_SIZE + BOX_SIZE, box_y * BOX_SIZE + BOX_SIZE), line_color='black', fill_color='black')

window.close()