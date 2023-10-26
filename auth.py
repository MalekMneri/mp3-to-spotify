"""auth and verification functions"""
import os
import sys

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
redirect_url = os.environ.get('SPOTIFY_REDIRECT_URI')


def check_args():
    """Verifies input"""
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
    """redirects to callback path to authenticate user"""
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_url,
        scope='playlist-modify-public playlist-modify-private',
        open_browser=False
    )
    return spotipy.Spotify(auth_manager=auth_manager)
