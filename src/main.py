import PySimpleGUI as sg
import random
import string

from engine import Engine
import time
import threading

sg.theme('DarkAmber')
sg.theme('SystemDefault')

CANVAS_SIZE = (20, 20)
WORLD_SIZE = (CANVAS_SIZE[0], CANVAS_SIZE[1], 20)
BOX_SIZE = 25

layout = [
    [sg.Text("Multidimensional Conway's Game of Life"), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((CANVAS_SIZE[0]*BOX_SIZE, CANVAS_SIZE[1]*BOX_SIZE), (0, CANVAS_SIZE[1]*BOX_SIZE), (CANVAS_SIZE[0]*BOX_SIZE, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False)],
    [sg.Button('Start'), sg.Button("Random"), sg.Button('Stop'), sg.Button('Exit')]
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
            if data[x,y,0] == 1:
                g.draw_rectangle((x * BOX_SIZE, y * BOX_SIZE), (x * BOX_SIZE + BOX_SIZE, y * BOX_SIZE + BOX_SIZE), line_color='black', fill_color='black')
            else:
                g.draw_rectangle((x * BOX_SIZE, y * BOX_SIZE), (x * BOX_SIZE + BOX_SIZE, y * BOX_SIZE + BOX_SIZE), line_color='black', fill_color='white')

def engine_thread_func(window, world, event):
    while not event.is_set():
        time.sleep(0.5)
        world.epoch()
        update_graph(window['-GRAPH-'], world.data)

stop_event = None

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    mouse = values['-GRAPH-']

    if event == 'Random':
        world = Engine.random(WORLD_SIZE)
        update_graph(g, world.data)
    elif event == 'Start':
        stop_event = threading.Event()
        threading.Thread(target=engine_thread_func, args=(window, world, stop_event), daemon=True,).start()
    elif event == 'Stop':
        if stop_event:
            stop_event.set()
    elif event == '-GRAPH-':
        if mouse == (None, None):
            continue
        update_graph(g, world.data)

window.close()