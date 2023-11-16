import keys
import spotipy
import requests
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import Search, YouTube


user_name = 'Shiv'
client_id = keys.CLIENT_ID
client_Secret = keys.SECRET_KEY
redirect_uri = 'http://google.com/callback/' 

yt_query = 'https://www.youtube.com/watch?v='

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
        result = track_name, track_uri.split(':')[2]
        tracks.append(result)

    return tracks

def get_isrc_id(test_id):
    # Converts Spotify song id to ISRC id
    song_data = spotify_obj.track(test_id)
    return song_data['external_ids']['isrc']



# pprint(get_tracks())
tracks = get_tracks()
test_id = tracks[0][1]
isrc_id = get_isrc_id(test_id)


# Search the video on Youtube using isrc id
search_obj = Search(isrc_id)
videoId = str(search_obj.results).split('=')[1].rstrip('>]')

# Search the video on youtube using link formed using videoId
yt_query+=str(videoId)
yt_object = YouTube(yt_query)

# Filter the desired Stream object which is in audio format
thing = str(yt_object.streams.filter(mime_type='audio/mp4')[0])

# Extracting the tag from the Stream object
tag = (((((thing.rstrip('>')).lstrip('<')).split(' ')[1]).split('=')[1])).strip('"')

# Download the video using the tag
audio = yt_object.streams.get_by_itag(tag)  
audio.download()
print("Audio downlaoded!")




