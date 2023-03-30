import os
from auth import get_token, check_args, auth, add_tracks_to_playlist
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
count = 0
for file in os.listdir(folder):
    if file.endswith('.mp3'):
        search = get_search(folder, file)
        results = sp.search(q=search, type='track', limit=1)

        if len(results['tracks']['items']) == 0:
            print('track not found!, ' + Fore.RED + search + Fore.RESET)
            continue
        #with open(f"batch_{batchIndex}.txt", 'a') as f:
        #    f.write(results['tracks']['items'][0]['uri'] + ',')
        #    count += 1
        trackIds.append(results['tracks']['items'][0]['uri'])
        print(trackIds)
        add_tracks_to_playlist(playlist_id, trackIds)
        #sp.playlist_add_items(playlist_id=playlist_id, items=trackIds)
        break
        #if len(trackIds) >= 90:
        #    sp.playlist_add_items(playlist_id=playlist_id, items=trackIds)
        #    trackIds.clear()
        #    batchIndex += 1
        #    print(f"batch: {batchIndex} added!")
