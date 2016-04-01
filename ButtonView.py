# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/5774800525983744

import ui

class ButtonView(ui.View):
    def __init__(self, title=None):
        w, h = ui.get_screen_size()
        self.frame = (0, 0, w, h)
        self.counter = 0
        self.add_subview(self.make_button(title))
    
    def action(self, sender):
        self.counter += 1
        sender.title = str(self.counter)

    def make_button(self, title=None):
        button = ui.Button(title=title or 'Tap me!')
        button.action = self.action
        button.flex = 'WH'
        button.frame = self.bounds
        return button

if __name__ == '__main__':
    single_button = False

    if single_button:
        ButtonView().present()
    else:
        import string
        view = ui.View()
        view.present()
        buttons_per_row = 13
        buttons_per_col = 2
        w = view.width / buttons_per_row
        h = view.height / buttons_per_col
        for i, letter in enumerate(string.ascii_lowercase):
            button_view = ButtonView(title=letter)
            #button_view.border_width = 1
            #button_view.border_color = 'white'
            button_view.frame = (i % buttons_per_row * w, i // buttons_per_row * h, w, h)
            view.add_subview(button_view)
        
