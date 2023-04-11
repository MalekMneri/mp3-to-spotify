# Description
This is a script to add your local mp3 files to your spotify playlist.
# Installation
To configure this project you'll need to:
- create a virtual environment using:<br>

`python -m venv my-venv`
- run the virtual environment:<br>

`./venv/Scripts/activate` or `source /venv/bin/activate` for Linux 
- install the dependencies using: 

`pip install -r requirements.txt`
- create a .env file and update it with your client id, secret, playlist id and redirect url that you get from [here](https://developer.spotify.com/):<br> 

`cp .env.dev .env`

Finally run: <br>

`python spotify.py <path/to/your/music/folder>`