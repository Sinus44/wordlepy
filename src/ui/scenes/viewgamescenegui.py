import src.gui as gui
from .palette import palette

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()

size = (500, 700)
matrix_size = 6, 5
margin = 40

cells = []

layout = gui.Layout()

btn_size = ((size[0] - margin * 2) / matrix_size[0], (size[1] - margin * 2 - 200) / matrix_size[1])
plane_size = (size[0] - margin * 2), (size[1] - margin * 2 - 200)

background = gui.Rect()
background.style.set_property("normal", "color", palette[0])
background.size = size
background.render()
layout.add_element(background)

for i in range(matrix_size[1]):
    cells.append([])
    for j in range(matrix_size[0]):
        btn = gui.Button()
        btn.position = (plane_size[0] / matrix_size[0] * j + margin, plane_size[1] / matrix_size[1] * i + margin)
        btn.size = btn_size
        btn.text = ""
        btn.style.set_property("normal", "outline_enable", True)
        btn.style.set_property("normal", "font_size", 32)
        btn.style.set_property("normal", "font_bold", True)
        btn.style.set_property("hovered", "outline_color", palette[10])
        cells[i].append(btn)

layout.add_elements(*sum(cells, []))

menu_button = gui.Button()
menu_button.text = "Меню"
menu_button.position = (0, 0)
menu_button.size = ((size[0] - margin * 2) / 4, 40)
menu_button.style.set_property("normal", "font_size", 18)
menu_button.style.set_property("normal", "outline_enable", False)
menu_button.style.set_property("hovered", "background_color", palette[1])
menu_button.render()

label = gui.Label()
label.text = ""
label.position = (0, 0)
label.size = (size[0], margin)
label.style.set_property("normal", "font_size", 25)
label.render()
layout.add_element(label)
