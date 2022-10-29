import PySimpleGUI as sg
import random
import string

from engine import Engine

sg.theme('DarkAmber')
sg.theme('SystemDefault')

CANVAS_SIZE = (20, 20)
BOX_SIZE = 25

layout = [
    [sg.Text("Multidimensional Conway's Game of Life"), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((CANVAS_SIZE[0]*BOX_SIZE, CANVAS_SIZE[1]*BOX_SIZE), (0, CANVAS_SIZE[1]*BOX_SIZE), (CANVAS_SIZE[0]*BOX_SIZE, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False)],
    [sg.Button('Start'), sg.Button("Random"), sg.Button('Exit')]
]

window = sg.Window('Window Title', layout, finalize=True)

g = window['-GRAPH-']

for row in range(CANVAS_SIZE[1]):
    for col in range(CANVAS_SIZE[0]):
        g.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black')

world = Engine(CANVAS_SIZE)


def update_graph(g, data):
    width, height = CANVAS_SIZE
    for x in range(width):
        for y in range(height):
            if data[x,y]:
                g.draw_rectangle((x * BOX_SIZE, y * BOX_SIZE), (x * BOX_SIZE + BOX_SIZE, y * BOX_SIZE + BOX_SIZE), line_color='black', fill_color='black')
            else:
                g.draw_rectangle((x * BOX_SIZE, y * BOX_SIZE), (x * BOX_SIZE + BOX_SIZE, y * BOX_SIZE + BOX_SIZE), line_color='black', fill_color='white')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    mouse = values['-GRAPH-']

    if event == 'Random':
        world = Engine.random(CANVAS_SIZE)
        update_graph(g, world.data)

    if event == '-GRAPH-':
        if mouse == (None, None):
            continue
        update_graph(g, world.data)

window.close()