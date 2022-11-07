# spotify-to-yt-music
Import your Spotify playlists to YouTube Music.
Work in progress!



## Required dependencies

* [`spotipy`](https://github.com/spotipy-dev/spotipy)
* [`ytmusicapi`](https://github.com/sigma67/ytmusicapi)
* [`thefuzz`](https://github.com/seatgeek/thefuzz)

## Recommended dependencies

* [`Levenshtein`](https://github.com/maxbachmann/python-Levenshtein) (For faster computation with thefuzz)


## How to use
1. Fetch your Spotify credentials [(tutorial)](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/) and put them in ```music.py```
2. Create ```headers_auth.json``` with your request header from YT music. [Tutorial](https://ytmusicapi.readthedocs.io/en/stable/setup.html)
