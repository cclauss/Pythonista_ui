# ui View for the top ten iTunes songs.
# This code only seems to run half the time.  Pull requests gladly accepted.

# coding: utf-8

import feedparser, ui

url = 'https://itunes.apple.com/us/rss/topsongs/limit=10/xml'

def get_image_urls(itunes_url):
    for entry in feedparser.parse(itunes_url).entries:
         yield entry['summary'].partition('src="')[2].partition('"')[0]

class TopTenView(ui.View):
    def __init__(self, image_urls):
        self.present()
        for i, url in enumerate(image_urls):
            image_view = ui.ImageView()
            image_view.load_from_url(url)
            self.add_subview(image_view)
            image_view.x = (i % 5) * 128 + 10
            image_view.y = (i / 5) * 128 + 10

TopTenView(get_image_urls(url))
