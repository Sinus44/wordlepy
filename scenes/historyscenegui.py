import copy

import gui

# Layout
# Test layout
# layout = layout
# Final layout
layout = gui.Layout()

palette = [
    (20, 20, 20),  # 0. Empty cell color / background 1
    (120, 120, 120),  # 1. No cell color / button hovered
    (230, 217, 80),  # 2. IN word cell color / yellow
    (110, 250, 132),  # 3. Position cell color / green
    (40, 40, 40),  # 4. background 2
    (70, 70, 70),  # 5. button background
    (201, 36, 18),  # 6. remove button back / red
    (237, 83, 66),  # 7. remove button hovered / light red
]

EMPTY = palette[0]
NO = palette[1]
IN_WORD = palette[2]
POSITION = palette[3]

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

title = gui.Label()
title.text = "HISTORY"
title.position = (0, 0)
title.size = (size[0], ph * 10)
title.style.set_property("normal", "font_size", int(ph * 6))
title.style.set_property("normal", "font_name", "")
title.render()
layout.add_element(title)

btn_style = gui.ButtonStyle()
btn_style.set_property("normal", "background_color", palette[5])
btn_style.set_property("hovered", "background_color", palette[1])
btn_style.set_property("disabled", "background_color", palette[0])
btn_style.set_property("normal", "font_size", 25)

btn_size = (60 * pw, 10 * ph)
btn_margin = 3 * ph

back_button = gui.Button()
back_button.position = (1 * pw, 1 * ph)
back_button.size = (30 * pw, 5 * ph)
back_button.text = "BACK"
back_button.style = copy.deepcopy(btn_style)
back_button.render()
layout.add_element(back_button)

clear_button = gui.Button()
clear_button.position = ((100 - 1 - 30) * pw, 1 * ph)
clear_button.size = (30 * pw, 5 * ph)
clear_button.text = "CLEAR"
clear_button.style = copy.deepcopy(btn_style)
clear_button.render()
layout.add_element(clear_button)

slide = gui.SlidePanel()
slide.position = (0, 10 * ph)
slide.size = (100 * pw, 80 * ph)
slide.style.set_property("normal", "align", "vertical")
layout.add_element(slide)

show_button = gui.Button()
show_button.position = (35 * pw, 92.5 * ph)
show_button.size = (30 * pw, 5 * ph)
show_button.text = "SHOW"
show_button.enable = False
show_button.style = copy.deepcopy(btn_style)
show_button.render()
layout.add_element(show_button)
