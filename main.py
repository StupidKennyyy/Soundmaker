from local_player import AudioPlayer
from GUI import SoundmakerGUI

Player = AudioPlayer()

GUI = SoundmakerGUI(Player)
GUI.run()
