import PySimpleGUI as sg

BOX_SIZE = 25


def create_window(canvas_size):
    layout = [
        [
            sg.Text("Multidimensional Conway's Game of Life"),
            sg.Text("", key="-OUTPUT-"),
        ],
        [
            sg.Graph(
                (canvas_size[0] * BOX_SIZE, canvas_size[1] * BOX_SIZE),
                (0, canvas_size[1] * BOX_SIZE),
                (canvas_size[0] * BOX_SIZE, 0),
                key="-GRAPH-",
                change_submits=True,
                drag_submits=False,
            )
        ],
        [sg.Button("Start"), sg.Button("Random"), sg.Button("Stop"), sg.Button("Exit")],
    ]
    window = sg.Window("Window Title", layout, finalize=True)
    g = window["-GRAPH-"]

    for row in range(canvas_size[1]):
        for col in range(canvas_size[0]):
            g.draw_rectangle(
                (col * BOX_SIZE, row * BOX_SIZE),
                (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE),
                line_color="black",
            )

    return window


def update_graph(window, data):
    print(data.shape)
    width, height = data.shape
    g = window["-GRAPH-"]
    for x in range(width):
        for y in range(height):
            if data[x, y] == 1:
                g.draw_rectangle(
                    (x * BOX_SIZE, y * BOX_SIZE),
                    (x * BOX_SIZE + BOX_SIZE, y * BOX_SIZE + BOX_SIZE),
                    line_color="black",
                    fill_color="black",
                )
            else:
                g.draw_rectangle(
                    (x * BOX_SIZE, y * BOX_SIZE),
                    (x * BOX_SIZE + BOX_SIZE, y * BOX_SIZE + BOX_SIZE),
                    line_color="black",
                    fill_color="white",
                )
