import tkinter as tk
from local_player import AudioPlayer


class SoundmakerGUI:
    def __init__(self, player: AudioPlayer):

        # Player
        self.player = player
        self.player.load()

        # TK
        self.root = tk.Tk()

        self.root.title("Soundmaker")
        self.root.geometry("250x100")

        icon = tk.PhotoImage(file="soundmaker_icon.png")
        self.root.iconphoto(False, icon)

        # Buttons
        btn_play = tk.Button(self.root, text="Play", command=self.player.play)
        btn_pause = tk.Button(self.root, text="Pause", command=self.player.pause)
        btn_next = tk.Button(self.root, text="Next", command=self.player.next)
        btn_previous = tk.Button(self.root, text="Previous", command=self.player.previous)

        # Centering with a 3-column grid
        self.root.grid_columnconfigure(0, weight=1)  # left spacer
        self.root.grid_columnconfigure(1, weight=1)  # center area
        self.root.grid_columnconfigure(2, weight=1)  # right spacer
         
        btn_play.grid(row=0, column=1, padx=10, pady=10)      
        btn_previous.grid(row=1, column=0, padx=5, pady=10)
        btn_pause.grid(row=1, column=1, padx=10, pady=10)      
        btn_next.grid(row=1, column=2, padx=10, pady=10)



    def run(self):
        self.root.mainloop()
    




