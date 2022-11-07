import spotipy
import music
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import credential
from thefuzz import fuzz


def cred_setup():
    credential.Credential()


def get_playlist_tracks(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    songs = playlist['tracks']['items']
    list_for_songs = []
    dict_for_albums = {}
    for song in songs:
        current_song_name = song['track']['name']
        current_song_artist = song['track']['artists'][0]['name']
        list_for_songs.append(current_song_name)
        dict_for_albums[current_song_name] = current_song_artist
    return list_for_songs, dict_for_albums


def setup_all_spotify_information(sp):
    info = music.MusicInfo()
    playlists_dict = {}
    songs_names_and_artists = {}
    playlists_titles_and_descriptions = {}
    playlists = sp.current_user_playlists(50)['items']

    for playlist in playlists:
        playlists_dict[playlist['name']] = get_playlist_tracks(playlist['id'], sp)[0]
        songs_names_and_artists.update(get_playlist_tracks(playlist['id'], sp)[1])
        playlists_titles_and_descriptions[playlist['name']] = playlist['description']

    info.spotify_playlists_and_their_songs = playlists_dict
    info.spotify_songs_and_artists = songs_names_and_artists
    info.spotify_playlists_titles_and_descriptions = playlists_titles_and_descriptions
    return info


def main():
    cred_setup()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-public'))
    yt = YTMusic("headers_auth.json")
    info = setup_all_spotify_information(sp)

    for playlist_title in info.spotify_playlists_and_their_songs:
        playlist_songs = info.spotify_playlists_and_their_songs[playlist_title]
        yt_playlist = yt.create_playlist(title=playlist_title,
                                         description=info.spotify_playlists_titles_and_descriptions[playlist_title])
        youtube_video_ids = []
        for song_title in playlist_songs:
            current_artist_from_spotify = str(info.spotify_songs_and_artists[song_title]).lower()
            yt_song = yt.search(query=f"{song_title} {info.spotify_songs_and_artists[song_title]}",
                                filter='songs', ignore_spelling=True)
            video_id = get_current_video_id(current_artist_from_spotify, yt_song, song_title)
            if video_id is not None:
                youtube_video_ids.append(video_id)

        if youtube_video_ids:
            yt.add_playlist_items(playlistId=yt_playlist, videoIds=youtube_video_ids)


def get_current_video_id(current_artist_from_sp, yt_song, song_title):
    for song_result in yt_song:
        for current_yt_artist in song_result['artists']:
            name = str(current_yt_artist['name']).lower()
            if name == current_artist_from_sp:
                similarity = fuzz.ratio(song_result['title'], song_title)
                if similarity >= 50:
                    return song_result['videoId']


if __name__ == '__main__':
    main()
