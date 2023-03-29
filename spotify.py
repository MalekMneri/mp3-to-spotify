import os
from auth import getToken, checkArgs, auth
from mutagen.mp3 import MP3
from colorama import Fore
from dotenv import load_dotenv

load_dotenv()
playlist_id = os.environ.get('PLAYLIST_ID')

folder = checkArgs()
sp = auth()

# token = getToken()

print('Running Script in folder: ' + folder)
trackIds = []
batchIndex = 0
offsetIndex = 10
for file in os.listdir(folder):
    if offsetIndex <= 20:
        offsetIndex += 1
        continue

    if file.endswith('.mp3'):
        audio = MP3(folder + '/' + file)
        title = audio.get("TIT2").text[0]
        artist = audio.get("TPE1").text[0]
        search = title + ' ' + artist
        print('adding ' + Fore.CYAN + file + Fore.RESET + ' as: \'' + Fore.CYAN + search + Fore.RESET + '\'')
        results = sp.search(q=search, type='track', limit=1)
        if len(results['tracks']['items']) == 0:
            print('track not found!, ' + Fore.RED + search + Fore.RESET)
            continue
        else:
            print(results['tracks']['items'][0]['name'])
        #trackIds.append(results['tracks']['items'][0]['uri'])
        #sp.playlist_add_items(playlist_id, results['tracks']['items'][0]['uri'])
        break
        # if len(trackIds) >= 100:
        #     sp.playlist_add_items(playlist_id, trackIds)
        #     trackIds.clear()
        #     batchIndex += 1
        #     print(f"batch: {batchIndex} added!")
# sp.playlist_add_items(playlist_id, trackIds)
