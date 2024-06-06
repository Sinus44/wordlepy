import copy

import src.gui as gui
from .palette import palette

# Layout
# Test layout
# layout = layout
# Final layout
layout = gui.Layout()

# Size
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
title.text = "WORDLE"
title.position = (0, 0)
title.size = top_background.size
title.style.set_property("normal", "font_size", int(ph * 8))
title.style.set_property("normal", "font_name", "")
title.render()
layout.add_element(title)

title_bottom = gui.Label()
title_bottom.position = (0, size[1] - ph * 5)
title_bottom.text = "v1.3.0 pre 4 Sinus44"
title_bottom.size = down_background.size
title_bottom.style.set_property("normal", "horizontal_align", "left")
title_bottom.style.set_property("normal", "font_size", int(ph * 6))
title_bottom.style.set_property("normal", "font_color", palette[5])
title_bottom.style.set_property("normal", "font_name", "")
title_bottom.render()
layout.add_element(title_bottom)

btn_style = gui.ButtonStyle()
btn_style.set_property("normal", "background_color", palette[5])
btn_style.set_property("hovered", "background_color", palette[1])
btn_style.set_property("disabled", "background_color", palette[0])
btn_style.set_property("normal", "font_size", 25)

btn_size = (60 * pw, 10 * ph)
btn_margin = 3 * ph

start_button = gui.Button()
start_button.position = (half_size[0] - btn_size[0] / 2, half_size[1] / 4 + btn_size[1] + btn_margin * 1)
start_button.size = btn_size
start_button.text = "START"
start_button.style = copy.deepcopy(btn_style)
start_button.style.set_property("hovered", "background_color", palette[3])
start_button.render()
layout.add_element(start_button)

history_button = gui.Button()
history_button.position = (half_size[0] - btn_size[0] / 2, half_size[1] / 4 + btn_size[1] * 2 + btn_margin * 2)
history_button.size = btn_size
history_button.text = "HISTORY"
history_button.style = btn_style
history_button.enable = True
history_button.render()
layout.add_element(history_button)

settings_button = gui.Button()
settings_button.position = (half_size[0] - btn_size[0] / 2, half_size[1] / 4 + btn_size[1] * 3 + btn_margin * 3)
settings_button.size = btn_size
settings_button.text = "SETTINGS"
settings_button.style = btn_style
settings_button.enable = False
settings_button.render()
layout.add_element(settings_button)

about_button = gui.Button()
about_button.position = (half_size[0] - btn_size[0] / 2, half_size[1] / 4 + btn_size[1] * 4 + btn_margin * 4)
about_button.size = btn_size
about_button.text = "ABOUT"
about_button.style = btn_style
about_button.enable = False
about_button.render()
layout.add_element(about_button)

exit_button = gui.Button()
exit_button.position = (half_size[0] - btn_size[0] / 2, half_size[1] / 4 + btn_size[1] * 5 + btn_margin * 5)
exit_button.size = btn_size
exit_button.text = "EXIT"
exit_button.style = copy.deepcopy(btn_style)
exit_button.style.set_property("hovered", "background_color", palette[7])
exit_button.render()
layout.add_element(exit_button)
