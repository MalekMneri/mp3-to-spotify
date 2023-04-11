import os
from auth import check_args, auth
from colorama import Fore
from dotenv import load_dotenv
from helpers import get_search

load_dotenv()
playlist_id = os.environ.get('PLAYLIST_ID')

folder = check_args()
sp = auth()

print('Running Script in folder: ' + folder)
trackIds = []
batchIndex = 0
for file in os.listdir(folder):
    if file.endswith('.mp3'):
        search = get_search(folder, file)
        results = sp.search(q=search, type='track', limit=1)
        if len(results['tracks']['items']) == 0:
            print('track not found!, ' + Fore.RED + search + Fore.RESET)
            continue

        trackIds.append(results['tracks']['items'][0]['uri'])
        if len(trackIds) >= 100:
            sp.playlist_add_items(playlist_id=playlist_id, items=trackIds)
            trackIds.clear()
            batchIndex += 1
            print(f"batch: {batchIndex} added!")
sp.playlist_add_items(playlist_id=playlist_id, items=trackIds)
