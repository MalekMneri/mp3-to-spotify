import base64
import os
import sys

import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

load_dotenv()
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
redirect_url = os.environ.get('SPOTIFY_REDIRECT_URI')


def get_token():
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return auth_manager.get_access_token()['access_token']


def add_tracks_to_playlist(playlist_id, tracks):
    auth_header = base64.b64encode((client_id + ':' + client_secret).encode('ascii')).decode('ascii')
    auth_options = {
        'url': f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",
        'headers': {
            'Authorization': 'Bearer ' + get_token()
        },
        'data': {
           'uris': ','.join(tracks)
        }
    }
    response = requests.post(**auth_options)
    print(response.json())
def check_args():
    args = sys.argv[1:]
    if len(args) == 0:
        print('please specify folder')
        sys.exit(1)
    folder = sys.argv[1:][0]
    if not os.path.isdir(folder):
        print('no such directory: ' + folder)
        sys.exit(1)
    return folder


def auth():
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    #auth_manager = SpotifyOAuth(
    #   client_id=client_id,
    #   client_secret=client_secret,
    #   redirect_uri=redirect_url,
    #   scope='playlist-modify-public',
    #)
    token = auth_manager.get_access_token()
    print(token)
    return spotipy.Spotify(auth_manager=auth_manager)
