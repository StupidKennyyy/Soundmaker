from pathlib import Path
import vlc

def GetSongsList() -> list:
    
    dir = Path("songs").absolute()

    songs = []

    for file_path in dir.iterdir():
        if file_path.is_file() and file_path.suffix == ".mp3":
            songs.append(str(file_path.absolute()))
    
    return songs

#def GetMediaList():
