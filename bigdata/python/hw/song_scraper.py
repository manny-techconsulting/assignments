from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup as bsp
from time import sleep
import pandas as pd
import csv
import re
from azlyrics import songs

'''
This is semi working  as of June 19 2:50 PM
@Author: Emanuel Garcia

'''
SONG_LIST_URL = "http://www.song-list.net/{}/songs"
LYRICS_BASE_URL = "https://www.azlyrics.com/lyrics/{}/{}.html"
LYRICS_TEXT_FILE = "lyrics.txt"
LYRICS_NOT_FOUND = []
DELAY = 3
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

def get_list_of_songs_by_artists(artists):
    
    """
    Arguments: A List of artists
    This function takes a list of artist names to get a list of song names to be used for
    AZ LYRICS.
    The text will be preprocessed for url lookup.
    Return: A Dictionary of songs by artists <Artist, List[Songs]>
    """
    songs_by_artists_dict = {}
    for artist in artists:
        artist_song_url = SONG_LIST_URL.format(artist)
        print("Accessing URL:\t " + artist_song_url)
        req = urllib.request.Request(artist_song_url, headers={'User-Agent' : "Magic Browser"}) 
        con = urllib.request.urlopen( req )
        soup = bsp(con, 'html.parser')
        songs_list = soup.find_all('div','divTableCell songname')
        songs_by_artists_dict[artist] = []
        for songs in songs_list:
            song = songs.a.text
            numbers_in_brackets_removed = re.sub(r'\(.*\)',"",song)
            processed_text = re.sub(r'\W+', '', numbers_in_brackets_removed).lower()
            if processed_text not in songs_by_artists_dict[artist]:
                songs_by_artists_dict[artist].append(processed_text)
    return songs_by_artists_dict
        

def get_lyrics_of_artist_by_song(artists):
    list_of_dict = []
    i = 0
    for artist,songs in artists.items():
        for song in songs:
            lyrics_url = LYRICS_BASE_URL.format(artist,song)
            album = None
            text = None
            try:
                req = urllib.request.Request(lyrics_url, headers=headers) 
                con = urllib.request.urlopen(req)
                soup = bsp(con, 'html.parser')
                print(soup)
                lyrics_pointer = soup.find_all('div','ringtone')
                album = soup.find('div', attrs='songinalbum_title')
                print(album)
                print(lyrics_pointer)
                print(f'Sending request to {lyrics_url}')
            except LyricsNotFoundException:
                print(f'Lyrics not found for {song} by {artist}')
            finally:
                print(album)
                print(text)
                df_dict = {'artist' : artist, 'song' : song, 'album': album, 'lyrics': text}
                list_of_dict.append(df_dict)
                i += 1
                if i >10:
                    break
    return pd.DataFrame(list_of_dict)

def create_songs_df():
    df = pd.DataFrame(columns=['artist','album','song','lyrics'])
    return df

class LyricsNotFoundException(Exception):
    pass

if __name__  == "__main__":
    
    

    
    
    
    