import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from mutagen.mp3 import MP3
from colorama import Fore
import sys

args = sys.argv[1:]
if len(args) == 0:
    print('please specify folder')
    sys.exit(1)
folder = sys.argv[1:][0]
if not os.path.isdir(folder):
    print('no such directory: ' + folder)

load_dotenv()
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
playlist_id = os.environ.get('PLAYLIST_ID')
REDIRECT_URI = 'http://localhost:8000/callback'
SCOPE = 'user-read-private user-read-email playlist-modify-public'

auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=REDIRECT_URI,scope=SCOPE)
sp = spotipy.Spotify(auth_manager=auth_manager)

print('Running Script in folder: ' + folder)
trackIds = []
batchIndex = 0
for file in os.listdir(folder):
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

        trackIds.append(results['tracks']['items'][0]['uri'])
        if len(trackIds) >= 100:
            sp.playlist_add_items(playlist_id, trackIds)
            trackIds.clear()
            batchIndex += 1
            print(f"batch: {batchIndex} added!")
sp.playlist_add_items(playlist_id, trackIds)
