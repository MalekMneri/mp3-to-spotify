"""main file"""
import os
from colorama import Fore
from dotenv import load_dotenv
from helpers import get_search
from auth import check_args, auth

load_dotenv()
playlist_id = os.environ.get("PLAYLIST_ID")

FOLDER = check_args()
sp = auth()

print("Running Script in folder: " + FOLDER)
trackIds = []
BATCH_INDEX = 0

for file in os.listdir(FOLDER):
    if not file.endswith(".mp3"):
        continue

    search = get_search(FOLDER, file)
    results = sp.search(q=search, type="track", limit=1)

    if len(results["tracks"]["items"]) == 0:
        print(f"track {Fore.RED}{search} {Fore.RESET}was not found!")
        continue

    trackIds.append(results["tracks"]["items"][0]["uri"])

    if len(trackIds) >= 100:
        sp.playlist_add_items(playlist_id=playlist_id, items=trackIds)
        trackIds.clear()
        BATCH_INDEX += 1
        print(f"batch: {BATCH_INDEX} added!")

if len(trackIds) == 0 and BATCH_INDEX == 0:
    print(f"{Fore.RED}ERROR: {Fore.RESET}no mp3 files were found")
else:
    # add last batch
    sp.playlist_add_items(playlist_id=playlist_id, items=trackIds)
