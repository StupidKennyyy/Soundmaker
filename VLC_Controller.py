import vlc
import time

from songs import GetSongsList

class VLC_Controller:
    def __init__(self):
        self.instance = vlc.Instance()
        self.list_player = self.instance.media_list_player_new()
        self.media_list = self.instance.media_list_new()
        self.player = self.list_player.get_media_player()

    def load(self):
        songs = GetSongsList()

        for song_path in songs:
            self.media_list.add_media(self.instance.media_new(song_path))
        
        self.list_player.set_media_list(self.media_list)

        print(f"Loaded songs: {songs}")


    def play(self):
        self.list_player.play()

        while self.list_player.is_playing() == False:
            time.sleep(0.1)


    def pause(self):
        self.list_player.pause()


    def next(self):
        self.list_player.next()

    def previous(self):
        self.list_player.previous()


    
