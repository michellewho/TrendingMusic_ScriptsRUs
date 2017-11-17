import spotipy
from pandas.io.json import json_normalize
import requests
import json
import pandas as pd
# import top_100 from Jons_Script

#replace token
api_token = "BQBDHiVkjBmxeflcoli5TnhJDJMtZMB4D75ewqY9EuN27pQA8ITbxgAu2LofDozNpb1oH_tA_mTENcgPQTHRi6iq31f_rP4HQGWg6lTtXcXmSDbV-SNzilQAyogayxNsGk0d_Bpwy9QkJy4"


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
	artist = df.get_value(index, "Title")
	artist_altered = artist.replace(" ", "+")
	myList = getTrackId(name_altered, api_token)
	print(myList)
	if myList is not None:
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
	else: 
		return None

# Main
unique_songs = pd.read_csv('../data/unique_song_peakPos_6yr.csv')

size = len(unique_songs.index)

df_final = getDataframeForSingleSong(unique_songs, 0, api_token)

for x in range(1, size):
	df_individual = getDataframeForSingleSong(unique_songs, x, api_token)
	if df_individual is not None: 
		df_final = df_final.append(df_individual)
	else: 
		pass

df_final.to_csv("../data/spotify_data_final.csv")




# Error displayed

# ['1X9TyFXi9fiQgAIWJmSJrw', '1yxSLGMDHlW21z4YXirZDS']
# Traceback (most recent call last):
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/contrib/pyopenssl.py", line 441, in wrap_socket
#     cnx.do_handshake()
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/OpenSSL/SSL.py", line 1716, in do_handshake
#     self._raise_ssl_error(self._ssl, result)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/OpenSSL/SSL.py", line 1448, in _raise_ssl_error
#     raise SysCallError(errno, errorcode.get(errno))
# OpenSSL.SSL.SysCallError: (54, 'ECONNRESET')

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/connectionpool.py", line 601, in urlopen
#     chunked=chunked)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/connectionpool.py", line 346, in _make_request
#     self._validate_conn(conn)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/connectionpool.py", line 850, in _validate_conn
#     conn.connect()
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/connection.py", line 326, in connect
#     ssl_context=context)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/util/ssl_.py", line 329, in ssl_wrap_socket
#     return context.wrap_socket(sock, server_hostname=server_hostname)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/contrib/pyopenssl.py", line 448, in wrap_socket
#     raise ssl.SSLError('bad handshake: %r' % e)
# ssl.SSLError: ("bad handshake: SysCallError(54, 'ECONNRESET')",)

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/requests/adapters.py", line 440, in send
#     timeout=timeout
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/connectionpool.py", line 639, in urlopen
#     _stacktrace=sys.exc_info()[2])
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/urllib3/util/retry.py", line 388, in increment
#     raise MaxRetryError(_pool, url, error or ResponseError(cause))
# urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.spotify.com', port=443): Max retries exceeded with url: /v1/artists/1yxSLGMDHlW21z4YXirZDS (Caused by SSLError(SSLError("bad handshake: SysCallError(54, 'ECONNRESET')",),))

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "scrape_spotify_api_modified.py", line 95, in <module>
#     df_individual = getDataframeForSingleSong(unique_songs, x, api_token)
#   File "scrape_spotify_api_modified.py", line 80, in getDataframeForSingleSong
#     df_individual["Followers"] = getPopularityOrFollowers(artistId, api_token, False)
#   File "scrape_spotify_api_modified.py", line 50, in getPopularityOrFollowers
#     response = requests.get(api_url_base, headers = headers)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/requests/api.py", line 72, in get
#     return request('get', url, params=params, **kwargs)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/requests/api.py", line 58, in request
#     return session.request(method=method, url=url, **kwargs)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/requests/sessions.py", line 508, in request
#     resp = self.send(prep, **send_kwargs)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/requests/sessions.py", line 618, in send
#     r = adapter.send(request, **kwargs)
#   File "/Users/Michelle/anaconda3/lib/python3.6/site-packages/requests/adapters.py", line 506, in send
#     raise SSLError(e, request=request)
# requests.exceptions.SSLError: HTTPSConnectionPool(host='api.spotify.com', port=443): Max retries exceeded with url: /v1/artists/1yxSLGMDHlW21z4YXirZDS (Caused by SSLError(SSLError("bad handshake: SysCallError(54, 'ECONNRESET')",),))
