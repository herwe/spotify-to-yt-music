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
1. Fetch your [Spotify credentials](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/) and put them in ```credential.py```
2. Create ```headers_auth.json``` with your request header from [YT music](https://ytmusicapi.readthedocs.io/en/stable/setup.html).

## Beware of limitations
There are tons of limitations in the APIs. Please read the documentation for spotipy and ytmusicapi. 
