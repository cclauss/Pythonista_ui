# coding: utf-8

import string, ui

class CharCountView(ui.View):
    def __init__(self):
        self.background_color = 'white'
        self.name = 'Char count: Unicode chars are multiple bytes long'
        self.add_subview(ui.Label(name='chars'))
        self.add_subview(ui.Label(name='bytes'))
        for sv in self.subviews:
            sv.alignment = ui.ALIGN_CENTER
            sv.font = '<system>', 14
        text_view = ui.TextView(name='text')
        text_view.delegate = self
        text_view.font = '<system>', 24
        text_view.text = __file__.rpartition('/')[2][:-3] + ' Ü'
        self.add_subview(text_view)
        self.textview_did_change(text_view)
        self.present()

    def layout(self):
        x, y, w, h = self.bounds
        label_height = 20
        self['chars'].frame = x, y, w / 2, label_height
        self['bytes'].frame = x + w / 2, y, w / 2, label_height
        self['text'].frame = x, y + label_height,  w,  h - label_height

    def textview_did_change(self, textview):
        self['chars'].text = '{} chars'.format(len(textview.text))
        self['bytes'].text = '{} bytes'.format(len(bytes(textview.text)))

CharCountView()
