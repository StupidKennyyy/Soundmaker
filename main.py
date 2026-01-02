from audio.local_player import AudioPlayer
from gui.GUI import SoundmakerGUI

Player = AudioPlayer()
GUI = SoundmakerGUI(Player)
Player.set_root(GUI.root)
Player.process_commands()
GUI.run()