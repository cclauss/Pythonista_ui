# coding: utf-8

# http://omz-forums.appspot.com/pythonista/post/5809271396630528
# calculations are incorrect!!!

import ui

w, h = ui.get_screen_size()

text_view = ui.TextView()
text_view.alignment = ui.ALIGN_CENTER
text_view.center = (w/2, h/4)

button = ui.Button(title='Convert')
button.border_width = 2
button.center = (w/2, h/2)

label = ui.Label()
label.width = w
label.alignment = ui.ALIGN_CENTER
label.center = (w/2, 3*h/4)
label.number_of_lines = 4
label.text = '''Enter a temperature above and tap "Convert".

Swipe down with two fingers to quit the app.'''

view = ui.View(title='Temperature Converter')
view.add_subview(text_view)
view.add_subview(button)
view.add_subview(label)
view.present(hide_title_bar=True)

fmt = '''
{:g} degrees Fahrenheit is {:g} degrees Celsius.

{:g} degrees Celsius is {:g} degrees Fahrenheit.'''

def convert_action(sender):
    try:
        value = float(text_view.text)
    except ValueError:
        value = 50
        text_view.text = str(value)
    label.text = fmt.format(value, value * 1.2, value, value * 0.8)

button.action = convert_action
