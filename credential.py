import os
import secret


class Credential:
    def __init__(self):
        self.CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        self.REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
        os.environ['SPOTIPY_CLIENT_ID'] = secret.get_client_id()  # Client ID goes here
        os.environ['SPOTIPY_CLIENT_SECRET'] = secret.get_client_secret()  # Client Secret goes here
        os.environ['SPOTIPY_REDIRECT_URI'] = secret.get_redirect_uri()  # Redirect URI goes here
