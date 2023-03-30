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
    auth_header = base64.b64encode((client_id + ':' + client_secret).encode('ascii')).decode('ascii')
    auth_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Authorization': 'Basic ' + auth_header
        },
        'data': {
            'grant_type': 'client_credentials'
        }
    }
    response = requests.post(**auth_options)
    token = response.json()['access_token']
    return {"Authorization": "Bearer " + token}


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
    #auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url)
    return spotipy.Spotify(auth_manager=auth_manager)
