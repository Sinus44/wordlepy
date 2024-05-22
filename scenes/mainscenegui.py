import gui

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()

palette = [
    (20, 20, 20)
]

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
        btn.style.set_property("hovered", "outline_color", (255, 255, 255))
        cells[i].append(btn)

layout.add_elements(*sum(cells, []))

keyboard_button_size = 30
keyboard = []

for i in range(3):
    keyboard.append([])
    for j in range(11):
        btn = gui.Button()
        btn.position = (plane_size[0] / 11 * j + margin, 120 / 3 * i + margin + 500)
        btn.size = (keyboard_button_size, keyboard_button_size)
        btn.text = alphabet[i * 11 + j]
        btn.style.set_property("normal", "outline_enable", True)
        btn.style.set_property("normal", "font_size", 30)
        btn.style.set_property("normal", "outline_width", 1)
        btn.style.set_property("hovered", "outline_color", (255, 255, 255))
        keyboard[i].append(btn)

layout.add_elements(*sum(keyboard, []))

enter_button = gui.Button()
enter_button.text = "Подтвердить"
enter_button.enable = False
enter_button.size = ((size[0] - margin * 2) / 3, 40)
enter_button.style.set_property("normal", "outline_enable", True)
enter_button.style.set_property("normal", "font_size", 20)
enter_button.style.set_property("normal", "background_color", (52, 179, 72))
enter_button.style.set_property("hovered", "background_color", (120, 255, 142))
enter_button.style.set_property("disabled", "background_color", (0, 0, 0))
enter_button.render()

delete_button = gui.Button()
delete_button.text = "Удалить"
delete_button.enable = False
delete_button.size = ((size[0] - margin * 2) / 3, 40)
delete_button.style.set_property("normal", "outline_enable", True)
delete_button.style.set_property("normal", "font_size", 20)
delete_button.style.set_property("normal", "background_color", (201, 36, 18))
delete_button.style.set_property("disabled", "background_color", (0, 0, 0))
delete_button.style.set_property("hovered", "background_color", (237, 83, 66))
delete_button.render()

new_game_button = gui.Button()
new_game_button.text = "Новая игра"
new_game_button.position = (size[0] - margin - (size[0] / 2 - margin), 480)
new_game_button.size = ((size[0] - margin * 2) / 3, 40)
new_game_button.style.set_property("normal", "font_size", 20)
new_game_button.style.set_property("normal", "outline_enable", True)
new_game_button.style.set_property("hovered", "background_color", (120, 120, 120))

new_game_button.render()

slide = gui.SlidePanel()
slide.position = (margin, 480)
slide.size = (size[0] - margin * 2, 40)
slide.add_child(new_game_button)
slide.add_child(enter_button)
slide.add_child(delete_button)

layout.add_element(slide)
