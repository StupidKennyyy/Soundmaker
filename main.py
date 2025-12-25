from VLC_Controller import VLC_Controller

import time

player = VLC_Controller()
player.load()
player.play()

while True:

    key = input("> ").strip().lower()

    if key == "n":
        player.next()
    elif key == "b":
        player.previous()
    elif key == "m":
        player.pause()


