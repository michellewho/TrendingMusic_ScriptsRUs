import spotipy
from pandas.io.json import json_normalize
import requests
import json
import pandas as pd
# import top_100 from Jons_Script

api_token = "BQDfme_vdpYFJqnr7keJJcXQq9DdSh9OfFZGTeiqj4KHTTbZSdLV7uLqHmCSe_NrElIT4X4tXbm0z9KhkcWy2k1QXxfuUXfGxlZThYif0uAjY-amAtf6r7AtMWR2xDFM1_Hlp3twgQEB5qs-rENZ2uqjgMeYzRTX4uHrqg"

# How to get information for a SINGLE song
def getAudioFeatures(track_Id, api_token): 
	spotify = spotipy.Spotify(auth=api_token)
	uri = 'spotify:track:' + track_Id
	results = spotify.audio_features(uri)
	song_df = json_normalize(results)
	return song_df

# How to get trackId for a song
def getTrackId(song_title, api_token):
	api_url_base = "https://api.spotify.com/v1/search"
	query_params = "?q=" + song_title + "&type=track&market=US&limit=1"
	headers = {'Content-type': 'application/json',
				'Authorization': 'Bearer {0}'.format(api_token)}
	response = requests.get(api_url_base + query_params, headers = headers)

	if response.status_code == 200:
		json_info = json.loads(response.content.decode('utf-8'))
		temp = json_info['tracks']['items']
		if len(temp) != 0: 
			dictionary = temp[0]
			return dictionary['id']
		else:
			return None
	else:
		return None 

# get popularity of the artist
def getPopularity(song_id, api_token):
	api_url_base = "https://api.spotify.com/v1/tracks/" + song_id
	headers = {'Content-type': 'application/json',
				'Authorization': 'Bearer {0}'.format(api_token)}
	response = requests.get(api_url_base, headers = headers)

	if response.status_code == 200:
		json_info = json.loads(response.content.decode('utf-8'))
		print(json_info)
	else:
		return None


# How to get the DF of Spotify info 
def getDataframeForSingleSong(df, index, api_token):
	name = df.get_value(index, "SongTitle")
	name_altered = name.replace(" ", "+")
	artist = df.get_value(index, "Artist")
	artist_altered = artist.replace(" ", "+")
	trackId = getTrackId(name_altered, api_token)
	if trackId != None: 
		df_individual = getAudioFeatures(trackId, api_token)
		df_individual['song_title'] = name
		df_individual['artist_name'] = artist
		df_individual['PeakPos'] = df.get_value(index, "PeakPos")
		return df_individual
	else: 
		return None

# Main
unique_songs = pd.read_csv('uniqe_song_peakPos.csv')

size = len(unique_songs.index)


df_final = getDataframeForSingleSong(unique_songs, 0, api_token)

for x in range(1, size):
	df_individual = getDataframeForSingleSong(unique_songs, x, api_token)
	if df_individual is None: 
		pass
	else: 
		df_final = df_final.append(df_individual)

df_final.to_csv("spotify_data_final.csv")