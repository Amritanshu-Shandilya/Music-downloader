import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pytube
from pytube import Search, YouTube

import keys
from yt_toolkit import Youtube_Toolkit

class Spotify_Toolkit(Youtube_Toolkit):
# This class inherits Youtube_Toolkit that gives it functions to download songs, so it just needs to work with spoitfy side of things
    def __init__(self):
        super().__init__()

        # Parameters use for OAuth with spotipy
        self.user_name = keys.USER_NAME
        self.client_id = keys.CLIENT_ID
        self.secret = keys.SECRET_KEY
        self.redirect_uri = 'http://google.com/callback/'

        # OAuth with spotipy
        credential_manager = SpotifyClientCredentials(client_id= self.client_id, client_secret=self.secret)

        # Creating a spotipy object
        self.spotify_obj = spotipy.Spotify(client_credentials_manager=credential_manager)

        # Variables for storing the playlist data
        self.playlist_link = "https://open.spotify.com/playlist/3qpQXtFqUeR2c9HeQoP6ES?si=mbXKhy0dQ_qKFXa3-OBIkQ"
        self.playlist_uri = None

        # Variables to store the song data
        self.tracks = []
        self.song_data = {}

    def get_playlist_uri(self):
    # Extracts URI from the playlist link
        self.playlist_uri = self.playlist_link.split("/")[-1].split("?")[0]

    def get_tracks(self):
    # Fetches the names & uri of the songs in playlist
        self.get_playlist_uri()
        for track in self.spotify_obj.playlist_items(self.playlist_uri)["items"]:
            track_uri = track["track"]["uri"]
            track_name = track["track"]["name"]
            result = track_name, track_uri.split(':')[2]
            self.tracks.append(result)

    def vid_id(self, track_uri):
    # Converts track_uri to video id
        data = self.spotify_obj.track(track_uri)
        self.isrc_code = data['external_ids']['isrc']
        search_obj = Search(self.isrc_id)
        # generating video id
        self.vid_id = str(search_obj.results).split('=')[1].rstrip('>]')

        
        
    def create_the_dict(self):
    # Strores the track details in a dictionary 
        for track in self.tracks:
            track_name = track[0]
            track_uri = track[1]
            



    


def main():
# A simple unit test
    spotify_toolkit = Spotify_Toolkit()
    spotify_toolkit.get_tracks()
    spotify_toolkit.create_the_dict()
    # print(spotify_toolkit.tracks)
    print(spotify_toolkit.song_data)
    # print(spotify_toolkit.get_isrc_id('5XeFesFbtLpXzIVDNQP22n'))
    



if __name__ == '__main__':
    main()