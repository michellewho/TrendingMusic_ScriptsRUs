import spotipy
from pandas.io.json import json_normalize
import requests
import json
# import top_100 from Jons_Script

api_token = "BQDouyB3FWTU2NfefIZ3P3-xw_Ni2t1SwdJ7CZ43Sx-iexTxgMgmtXjxT_K7CxooACN59pO8MHtdn6N94bLPxpv8PSSn99FPrwbXDF72M8DU6BNs1L6vXhWvmJOK9lJ3uCgqKwobmpY4Xtv-2Qdr6NgKXS5e1rPZYVI"

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
		dictionary = temp[0]
		return dictionary['id']
	else:
		return none 

# Code to test my two methods (very disposable)
trackId = getTrackId("Feel+It+Still", api_token)
df = getAudioFeatures(trackId, api_token)
df.to_csv("test.csv")