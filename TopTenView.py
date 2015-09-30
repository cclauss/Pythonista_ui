# coding: utf-8

# ui.View subclass for the top ten iTunes songs.
# Pull requests gladly accepted.

import feedparser, requests, ui

url = 'https://itunes.apple.com/us/rss/topsongs/limit=10/xml'

def get_image_urls(itunes_url):
    for entry in feedparser.parse(itunes_url).entries:
        yield entry['summary'].partition('src="')[2].partition('"')[0]

class TopTenView(ui.View):
    def __init__(self, image_urls):
        self.present()
        for i, url in enumerate(image_urls):
            button = ui.Button()
            button.background_image = ui.Image.from_data(requests.get(url).content)
            button.border_width = 2
            button.x = (i % 5) * 128 + 10
            button.y = (i / 5) * 128 + 10
            button.width = button.height = 128
            self.add_subview(button)

TopTenView(list(get_image_urls(url)))
