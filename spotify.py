import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
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

print('Running Script on folder: ' + folder)
for file in os.listdir(folder):
    if file.endswith('.mp3'):
        audio = MP3(folder+'/'+file)
        title = audio.get("TIT2").text[0]
        artist = audio.get("TPE1").text[0]
        print('adding ' + Fore.RED+file + Fore.RESET+' as: \'' + Fore.CYAN+title + ' ' + artist + Fore.RESET+'\'')

#load_dotenv()
#client_id = os.environ.get('SPOTIFY_CLIENT_ID')
#client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
#
#client_creds_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#sp = spotipy.Spotify(client_credentials_manager=client_creds_manager)







#song_name = 'Wow. Post malone'
#results = sp.search(q=song_name, type='track', limit=1)
#print(results)
