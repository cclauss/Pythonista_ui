#http://trekcore.com/audio/warp/tng_warp4_clean.mp3
#http://trekcore.com/audio/warp/tng_warp_out4.mp3

import requests, sound, ui
#download sound effects from the web
url_fmt = 'http://trekcore.com/audio/warp/{}.mp3'
filenames = 'tng_warp_out4.caf tng_warp4_clean.caf'.split()
for filename in filenames:
    with open(filename, 'wb') as out_file:
        out_file.write(requests.get(url_fmt.format(filename.rstrip('.caf'))).content)
    sound.load_effect(filename)

def warp_action(sender):
    sound.play_effect(filenames[int(sender.value)])

view = ui.View(name = 'Captain Picard Wants Warp Speed')
sw = ui.Switch()
sw.action = warp_action
view.add_subview(sw)
view.present()
sw.center = view.center
