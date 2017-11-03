import pandas as pd

song_data = pd.read_csv('spotify_data.csv')

# Descriptive Statistics 
d = {}
d["dancibility_average"] = song_data["danceability"].mean()
d["acousticness_average"] = song_data["acousticness"].mean()
d["duration_ms_average"] = song_data["duration_ms"].mean()
d["energy_average"] = song_data["energy"].mean()
d["instrumentalness_average"] = song_data["instrumentalness"].mean()
d["key_mode"] = song_data["key"].mode()
d["liveness_mean"] = song_data["liveness"].mean()
d["loudness_mean"] = song_data["loudness"].mean()
d["speechiness_mean"] = song_data["speechiness"].mean()
d["tempo_mean"] = song_data["tempo"].mean()
d["time_signature_mode"] = song_data["time_signature"].mode()
d["valence_mean"] = song_data["valence"].mean()

descriptive_stats = pd.DataFrame(d)
print(descriptive_stats)

# Statistical Tests

# correlation between peak position and acousticness/dance/duration/energy/instrument/live/loud/speach/temp/valence
# asking for scatterplts from jon
danceability = song_data["danceability"]
print(danceability)