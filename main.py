import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import credential


def cred_setup():
    credential.Credential()


def get_playlist_tracks(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    songs = playlist['tracks']['items']
    list_for_songs = []
    for song in songs:
        list_for_songs.append(song['track']['name'])
    return list_for_songs


def main():
    cred_setup()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-public'))
    playlists = sp.current_user_playlists(50)['items']
    my_dict = {}
    for playlist in playlists:
        my_dict[playlist['name']] = get_playlist_tracks(playlist['id'], sp)

    for key in my_dict:
        print(key)
        print(my_dict[key])


if __name__ == '__main__':
    main()
