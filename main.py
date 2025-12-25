import vlc
import time

from songs import GetSongsList

instance = vlc.Instance()

songs = GetSongsList()

media_list = instance.media_list_new()

for song_path in songs:
    media_list.add_media(instance.media_new(song_path))
    
list_player = instance.media_list_player_new()
list_player.set_media_list(media_list)

###
player = list_player.get_media_player()

print(player)

list_player.play()

while list_player.is_playing() == False:
    time.sleep(0.1)
    


while list_player.is_playing():
    time.sleep(10)
    print("Playing")
    media = player.get_media()
    print(media.get_mrl())
    print(list_player.next())
    
    
print("Stopped")
