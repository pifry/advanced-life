import PySimpleGUI as sg

from gui import create_window, update_graph

from engine import Engine
import time
import threading

# sg.theme('DarkAmber')
sg.theme("SystemDefault")

CANVAS_SIZE = (20, 20)
WORLD_SIZE = (CANVAS_SIZE[0], CANVAS_SIZE[1], 20)
BOX_SIZE = 25

window = create_window(CANVAS_SIZE)
world = Engine(CANVAS_SIZE)


def engine_thread_func(window, world, event):
    while not event.is_set():
        time.sleep(0.5)
        world.epoch()
        update_graph(window, world.get_flat_data())


stop_event = None

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    mouse = values["-GRAPH-"]

    if event == "Random":
        world = Engine.random(WORLD_SIZE)
        update_graph(window, world.get_flat_data())
    elif event == "Start":
        stop_event = threading.Event()
        threading.Thread(
            target=engine_thread_func,
            args=(window, world, stop_event),
            daemon=True,
        ).start()
    elif event == "Stop":
        if stop_event:
            stop_event.set()
    elif event == "-GRAPH-":
        if mouse == (None, None):
            continue
        update_graph(window, world.get_flat_data())

window.close()
