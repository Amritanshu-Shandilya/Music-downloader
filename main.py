import keys
import spotipy
import json
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials


user_name = 'Shiv'
client_id = keys.CLIENT_ID
client_Secret = keys.SECRET_KEY
redirect_uri = 'http://google.com/callback/' 

playlist_link = "https://open.spotify.com/playlist/3qpQXtFqUeR2c9HeQoP6ES?si=mbXKhy0dQ_qKFXa3-OBIkQ"

credential_manager = SpotifyClientCredentials(client_id= client_id, client_secret=client_Secret)
spotify_obj = spotipy.Spotify(client_credentials_manager=credential_manager)

def get_playlist_uri(playlist_link):
    "Extracts URI from the playlist link"
    return playlist_link.split("/")[-1].split("?")[0]


def get_tracks():
    tracks = []
    playlist_uri = get_playlist_uri(playlist_link)
    for track in spotify_obj.playlist_items(playlist_uri)["items"]:
        track_uri = track["track"]["uri"]
        track_name = track["track"]["name"]
        result = track_name, spotify_obj.audio_features(track_uri)
        tracks.append(result)

    return tracks


raw_data = get_tracks()
print(raw_data[0][0]+" : "+raw_data[0][1][0]['id'])
