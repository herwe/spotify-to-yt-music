import os


class Credential:
    def __init__(self):
        self.CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        self.REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
        os.environ['SPOTIPY_CLIENT_ID'] = ""                # Client ID goes here
        os.environ['SPOTIPY_CLIENT_SECRET'] = ""            # Client Secret goes here
        os.environ['SPOTIPY_REDIRECT_URI'] = ""             # Redirect URI goes here
