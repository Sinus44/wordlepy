import copy

import gui
from .palette import palette

layout = gui.Layout()

size = (500, 700)
half_size = (size[0] / 2, size[1] / 2)
pw = size[0] / 100
ph = size[1] / 100

main_background = gui.Rect()
main_background.position = (0, 0)
main_background.size = size
main_background.style.set_property("normal", "color", palette[4])
main_background.render()
layout.add_element(main_background)

top_background = gui.Rect()
top_background.position = (0, 0)
top_background.size = (size[0], ph * 10)
top_background.style.set_property("normal", "color", palette[0])
top_background.render()
layout.add_element(top_background)

down_background = gui.Rect()
down_background.position = (0, size[1] - ph * 5)
down_background.size = (size[0], ph * 5)
down_background.style.set_property("normal", "color", palette[0])
down_background.render()
layout.add_element(down_background)

title = gui.Label()
title.text = "SETTINGS"
title.position = (0, 0)
title.size = top_background.size
title.style.set_property("normal", "font_size", int(ph * 8))
title.style.set_property("normal", "font_name", "")
layout.add_element(title)

word_validate = gui.Checkbox()
word_validate.position = (100, 100)
word_validate.size = (300, 50)
word_validate.text = "Проверка слов на существование"
layout.add_element(word_validate)

history_checkbox = gui.Checkbox()
history_checkbox.position = (100, 160)
history_checkbox.size = (300, 50)
history_checkbox.text = "Ведение истории игр"

btn_style = gui.ButtonStyle()
btn_style.set_property("normal", "background_color", palette[5])
btn_style.set_property("hovered", "background_color", palette[1])
btn_style.set_property("disabled", "background_color", palette[0])
btn_style.set_property("normal", "font_size", 25)

back_button = gui.Button()
back_button.position = (1 * pw, 1 * ph)
back_button.size = (20 * pw, 5 * ph)
back_button.text = "BACK"
back_button.style = copy.deepcopy(btn_style)
back_button.style.set_property("normal", "font_name", "")
layout.add_element(back_button)

layout.add_element(history_checkbox)
