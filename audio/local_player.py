import vlc
import time
from pathlib import Path
from queue import Queue
import threading
from time_checking import time_checker
from tkinter import Tk

def GetSongsList() -> list:
    
    dir = Path("songs").absolute()

    songs = []

    for file_path in dir.iterdir():
        if file_path.is_file() and file_path.suffix == ".mp3":
            songs.append(str(file_path.absolute()))
    
    return songs



class AudioPlayer:
    def __init__(self):

        self.instance = vlc.Instance()
        self.list_player = self.instance.media_list_player_new()
        self.media_list = self.instance.media_list_new()
        self.player = self.list_player.get_media_player()
        self.msg_queue = Queue()
        self.root = None

        threading.Thread(target=time_checker.CheckTime, args=(self.msg_queue,), daemon=True).start()

        self.process_commands()

    # Load the songs into a medialist
    def load(self):

        songs = GetSongsList()

        for song_path in songs:
            self.media_list.add_media(self.instance.media_new(song_path))
        
        self.list_player.set_media_list(self.media_list)

        #print(f"Loaded songs: {songs}")

    def process_commands(self):

        try:
            while not self.msg_queue.empty():
                command = self.msg_queue.get_nowait()

                print(command)

                if command == "PLAY":
                    self.play()
                elif command == "STOP":
                    self.pause()

            if self.root:
                self.root.after(10000, self.process_commands)
        except Exception as e:
            print(f"Error while processing commands: {e}")

    def play(self):

        self.list_player.play()

        while self.list_player.is_playing() == False:
            time.sleep(0.1)

    # Pause/Resume
    def pause(self):
        self.list_player.pause()


    def next(self):
        self.list_player.next()

    def previous(self):
        self.list_player.previous()

    def get_state(self):
        print(self.list_player.get_state())

    def set_root(self, root: Tk):
        self.root = root
        print("Set root")

    def set_volume(self, volume: int):
        self.player.audio_set_volume(volume)