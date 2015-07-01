'''
Many people initially have difficulty formating their Python code so it
looks good in posts to the Pythonisa Forum. http://omz-forums.appspot.com
This script attempts to properly format your code with appropriate carrage
returns and backticks so that it is ready to post to the forum.
'''

import clipboard, console, ui

fmt = '\n\n```{}\n{}\n```\n'  # .format(language, post_text)

def text_is_python(in_text):
    for line in in_text.splitlines():
        line = line.partition('#')[0].strip() or '.'
        first_word = line.split()[0]
        if first_word == 'import':
            return True
        if first_word in ('class', 'def') and line.endswith('):'):
            return True
    return False

class ThreeBackticksView(ui.View):
    def __init__(self):
        self.present()
        self.add_subview(self.make_button())
        self.add_subview(self.make_label())
        self.add_subview(self.make_switch())
        self.add_subview(self.make_text_view())
        self.textview_did_change(self['text_view'])

    def make_button(self):
        button = ui.Button(title='Format the post')
        button.action = lambda sender: self.do_it()
        button.center = self.width * .75, 50
        button.tint_color = 'steelblue'
        return button

    def make_label(self):
        label = ui.Label(name='label')
        label.width = 234
        label.text = 'Post contains Python code?'
        label.text_color = 'steelblue'
        label.center = self.width * .20, 50
        return label

    def make_switch(self):
        switch = ui.Switch(name='python_code',
                           title='Post contains Python code?')
        switch.center = self.width * .30, 50
        switch.x = self['label'].x + self['label'].width
        return switch

    def make_text_view(self):
        text_view = ui.TextView(frame=self.bounds, name='text_view')
        text_view.y += 100
        text_view.height -= 100
        text_view.delegate = self
        text_view.text = clipboard.get()
        text_view.autocapitalization_type = ui.AUTOCAPITALIZE_NONE
        text_view.autocorrection_type = False
        text_view.spellchecking_type = False
        return text_view

    def textview_did_change(self, textview):
        self['python_code'].value = text_is_python(textview.text)

    def do_it(self):
        text = self['text_view'].text.rstrip()
        if text:
            lang = 'python' if self['python_code'].value else ''
            text = fmt.format(lang, text)
            clipboard.set(text)
            self['text_view'].text = text
            console.hud_alert('The post is now on your clipboard.')
            print(text)
        else:
            print('No user text.')

ThreeBackticksView()
