import requests
import re
import numpy as np
import matplotlib.pyplot as plt
import apikey


def lyrics_word_count_easy(artist, song, phrase):
    response = requests.get("https://api.lyrics.ovh/v1/" + artist + "/" + song)
    if response.status_code != 200:
        return -1

    lyrics = response.json()["lyrics"]
    count = re.findall(phrase, lyrics, re.IGNORECASE)
    return len(count)


def lyrics_word_count(artist, phrase):
    api_key = apikey.musixmatch_key;
    response = requests.get("http://api.musixmatch.com/ws/1.1/artist.search?apikey=" + api_key + "&q_artist=" + artist)
    if response.status_code != 200:
        return "Search for artist name failed."
    results = response.json()
    if len(results['message']['body']['artist_list']) == 0:
        return "No such artist found."
    artist_list = results['message']['body']['artist_list']
    artist_id = artist_list[0]['artist']['artist_id']

    response = requests.get("http://api.musixmatch.com/ws/1.1/artist.albums.get?apikey=" + api_key + "&artist_id=" + str(artist_id))
    if response.status_code != 200:
        return "Search for artist's album failed."
    results = response.json()
    if results['message']['body'] == '':
        return "No such albums found."
    album_list = results['message']['body']['album_list']
    album_id_list = []
    for album in album_list:
        album_id_list.append(album['album']['album_id'])

    track_name_list, track_name_list_raw = [], []
    for album_id in album_id_list:
        response = requests.get("http://api.musixmatch.com/ws/1.1/album.tracks.get?apikey=" + api_key + "&album_id=" + str(album_id))
        if response.status_code != 200:
            return "Search for album's tracks failed."
        results = response.json()
        if results['message']['body'] == '':
            return "No such tracks found."
        track_list = results['message']['body']['track_list']
        for track in track_list:
            name = track['track']['track_name']
            if name.lower() not in track_name_list:
                track_name_list.append(name.lower())
                track_name_list_raw.append(name)

    print(track_name_list_raw)

    count = 0
    for name in track_name_list_raw:
        song_count = lyrics_word_count_easy(artist, name, phrase)
        if song_count > 0:
            count += song_count
            print(name + " has " + str(song_count) + " counts of \"" + phrase + "\"")
        elif song_count == -1:
            print(name + " is not found in lyrics.ovh database.")
        else:
            print(name + " has 0 counts of \"" + phrase + "\"")

    return count

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28.,-22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])

    plt.subplot(2,1,1).set_title("LineGraph")
    plt.plot(x, y)
    plt.subplot(2,2,3).set_title("Histogram")
    plt.hist((x, y))
    plt.subplot(2,2,4).set_title("Scatter")
    plt.scatter(x, y)

    return plt.show()
