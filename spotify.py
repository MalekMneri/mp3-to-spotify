import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
print(os.getcwd())

client_creds_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_creds_manager)

#song_name = 'Wow. Post malone'
#results = sp.search(q=song_name, type='track', limit=1)
#print(results)
dir_list = os.listdir()

print("Files and directories in current folder :")

# prints all files
print(dir_list)
