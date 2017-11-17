import spotipy
from pandas.io.json import json_normalize
import requests
import json
import pandas as pd
# import top_100 from Jons_Script

api_token = "BQA2QCZpgezsHCAs1C6WqAj4_G9a-M8MOUg1jlj8RwMOeT7EFiWY8glG9vRjwmYtBldcwwEL6ltnITEHB3WuAFsEgMZbjqUHD1fu3XSeSI9ew7W4G7UMQcVyEVL7Sehl6v_Ft6dSXb_XcQoNhieFRU_tDwdoJM-wrmI"

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
			trackId = dictionary['id']
			artistId = dictionary["album"]
			forreal = artistId["artists"]
			fuck = forreal[0]
			artistId = fuck["id"]
			myList = [trackId, artistId]
			return myList
		else:
			return None
	else:
		return None 

# get popularity of the artist
def getPopularityOrFollowers(artist_id, api_token, isPopularity):
	api_url_base = "https://api.spotify.com/v1/artists/" + artist_id
	headers = {'Content-type': 'application/json',
				'Authorization': 'Bearer {0}'.format(api_token)}
	response = requests.get(api_url_base, headers = headers)

	if response.status_code == 200:
		json_info = json.loads(response.content.decode('utf-8'))
		if isPopularity: 
			return json_info["popularity"]
		else: 
			return json_info["followers"]["total"]
	else:
		return None


# How to get the DF of Spotify info 
def getDataframeForSingleSong(df, index, api_token):
	name = df.get_value(index, "SongTitle")
	name_altered = name.replace(" ", "+")
	artist = df.get_value(index, "Artist")
	artist_altered = artist.replace(" ", "+")
	myList = getTrackId(name_altered, api_token)
	if myList[0] is None:
		return None
	trackId = myList[0]
	artistId = myList[1]
	if trackId != None and artistId != None: 
		df_individual = getAudioFeatures(trackId, api_token)
		popularity = getPopularityOrFollowers(artistId, api_token, True)
		df_individual['song_title'] = name
		df_individual['artist_name'] = artist
		df_individual['PeakPos'] = df.get_value(index, "PeakPos")
		df_individual['Popularity'] = popularity
		df_individual["Followers"] = getPopularityOrFollowers(artistId, api_token, False)
		return df_individual
	else: 
		return None

# Main
unique_songs = pd.read_csv('unique_songs_6year.csv')

size = len(unique_songs.index)


df_final = getDataframeForSingleSong(unique_songs, 0, api_token)

for x in range(1, size):
	df_individual = getDataframeForSingleSong(unique_songs, x, api_token)
	if df_individual is None: 
		pass
	else: 
		df_final = df_final.append(df_individual)

df_final.to_csv("spotify_data_final.csv")
