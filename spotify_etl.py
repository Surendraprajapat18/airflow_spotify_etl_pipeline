import requests
import base64
import pandas as pd
import datetime
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials

currentDateTime = datetime.datetime.now()
dateTime = currentDateTime.strftime("%c")


def run_spotify_etl():
    # Scraping Artists Name
    url = 'https://kworb.net/itunes/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = [td for td in soup.find_all('td') if td.find('a')]
    list_of_artists = [td.find('a').text for td in title]

    # Spotify credentials
    client_id = 'd93c01e1a52d46fea273d42d1a59819b'
    client_secret = 'c273556539de4cdc852ed62e788eef85'

    # Initialize Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Extraction
    def get_artist_info(artist_name):
        results = sp.search(q='artist:' + artist_name, type='artist', limit=1)

        if results['artists']['items']:
            artist = results['artists']['items'][0]
            id = artist['id']
            name = artist['name']
            followers = artist['followers']['total']
            genre = artist.get('genres', ["NA"])
            popularity = artist['popularity']

            return {"id": id, "name": name, "followers": followers, "genre": genre, "popularity": popularity}

        return None

    artists_list = [get_artist_info(artist) for artist in list_of_artists]

    # Remove None values from the list (artists not found)
    artists_list = [artist for artist in artists_list if artist]

    df = pd.DataFrame(artists_list)
    df.to_csv('s3://surendra-airflow-spotify-data/artists_data.csv', index=False)

