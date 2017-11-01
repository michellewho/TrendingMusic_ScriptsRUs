# import top100names from jon's script
import spotipy
# import top_100 from Jons_Script
from pandas.io.json import json_normalize
import requests
import json
import re


<<<<<<< HEAD
=======
spotify = spotipy.Spotify(auth="BQDCdUSHznrFc9TieFUjmAbkrGFf-Fph0KsKLsuBKc6jkCRcGAUxW4yHSDhWhdyFnZPuLAWZE4pyyM_sC05Tvg")

>>>>>>> 07e9929c7b84c51b112e46fdd0a0ca8ead8b06ef
# How to get information for a SINGLE song
#uri = 'spotify:track:06AKEBrKUckW0KREUWRnvT'
#results = spotify.audio_features(uri)
#df = json_normalize(results)
#df.to_csv('data_for_specific_song.csv')

<<<<<<< HEAD
=======

# How to get Song ID (or Track ID) from the Top 100 Playlist - these keys are specific
# to the bill board top 100 2017

#url = 'spotify:playlist:2kpoUUJ5a4Cw3feTkFJhZ2'
#user = "1276640268"
#results2 = spotify.user_playlist(user_id=user, playlist_id="2kpoUUJ5a4Cw3feTkFJhZ2")
#df2 = json_normalize(results2)
#df2.to_csv('data_for_top_100.csv')


# now we need to make a method that gets all of the track ids from df2 and then
# gets the information from the first code chunk, appending that to a master dataframe


track_data = spotify.search('Feel+It+Still', market='US', limit=1, type='track')
track_json = json_normalize(track_data)
foobar = track_json.stringify()

foo = re.search(r"'id' : '.+'", foobar).group(0)
print(foo)

# extract Track Id and to string 

>>>>>>> 07e9929c7b84c51b112e46fdd0a0ca8ead8b06ef
