"""gets MP3 files' metadata"""
from mutagen.mp3 import MP3
from colorama import Fore


def get_search(folder, file):
    """concatenates artist and song title and returns a search string"""
    audio = MP3(folder + '/' + file)
    title = audio.get("TIT2").text[0]
    artist = audio.get("TPE1").text[0]
    search = title + ' ' + artist
    print(f"adding {Fore.CYAN}{file} {Fore.RESET} as: '{Fore.CYAN}{search} {Fore.RESET}'")
    return search
