import spotipy
from pandas.io.json import json_normalize



# How to get information for a SINGLE song
uri = 'spotify:track:06AKEBrKUckW0KREUWRnvT'
spotify = spotipy.Spotify(auth="BQBlLz9P1e0A5Ay3ybrts7SSJ-h3MgZpbH5LKPPvonuLARHZfcCfrJW6O4QDV__pzL17ampU-5cr8s56IN8rxg")
results = spotify.audio_features(uri)
df = json_normalize(results)
df.to_csv('data_for_specific_song.csv')


# How to get Song ID (or Track ID) from the Top 100 Playlist - these keys are specific
# to the bill board top 100 2017

url = 'spotify:playlist:2kpoUUJ5a4Cw3feTkFJhZ2'
user = "1276640268"
results2 = spotify.user_playlist(user, playlist_id="2kpoUUJ5a4Cw3feTkFJhZ2")
df2 = json_normalize(results2)
df2.to_csv('data_for_top_100.csv')

# now we need to make a method that gets all of the track ids from df2 and then
# gets the information from the first code chunk, appending that to a master dataframe
