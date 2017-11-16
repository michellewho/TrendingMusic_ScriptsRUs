import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import plotly 
plotly.tools.set_credentials_file(username='michellewho', api_key='WhPW7c0eUbIDJpAHl1nM')

song_data = pd.read_csv('spotify_data_final.csv')

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

# Statistical Tests

# correlation between peak position and acousticness/dance/duration/energy/instrument/live/loud/speach/temp/valence
# asking for scatterplts from jon

peakPos = song_data["PeakPos"]

danceability = song_data["danceability"]
acousticness = song_data["acousticness"]
duration_ms = song_data["duration_ms"]
energy  = song_data["energy"]
instrumentalness  = song_data["instrumentalness"]
liveness  = song_data["liveness"]
loudness  = song_data["loudness"]
speechiness  = song_data["speechiness"]
tempo  = song_data["tempo"]
time_signature  = song_data["time_signature"]
valence  = song_data["valence"]


danceabilityData = go.Scatter(
    y=peakPos,
    x=danceability,
    mode = 'markers'
)
layout = go.Layout(
    title='Danceability ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Danceability',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
danceabilityFig = go.Figure(data=[danceabilityData], layout=layout)
py.plot(danceabilityFig, filename='danceabilityscatter')

acousticnessData = go.Scatter(
    y = peakPos,
    x = acousticness,
    mode = 'markers'
)
layout = go.Layout(
    title='Acousticness ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Acousticness',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
acousticnessFig = go.Figure(data=[acousticnessData], layout=layout)
py.plot(acousticnessFig, filename='acousticnessscatter')

duration_msData = go.Scatter(
    y = peakPos,
    x = duration_ms,
    mode = 'markers'
)
layout = go.Layout(
    title='Duration ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Duration (ms)',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
duration_msFig = go.Figure(data=[duration_msData], layout=layout)
py.plot(duration_msFig, filename='durationmsscatter')

energyData = go.Scatter(
    y = peakPos,
    x = energy,
    mode = 'markers'
)
layout = go.Layout(
    title='Energy ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Energy',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
energyFig = go.Figure(data=[energyData], layout=layout)
py.plot(energyFig, filename='energyscatter')

instrumentalnessData = go.Scatter(
    y = peakPos,
    x = instrumentalness,
    mode = 'markers'
)
layout = go.Layout(
    title='Instrumentalness ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Instrumentalness',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
instrumentalnessFig = go.Figure(data=[instrumentalnessData], layout=layout)
py.plot(instrumentalnessFig, filename='instrumentalnessscatter')

livenessData = go.Scatter(
    y = peakPos,
    x = liveness,
    mode = 'markers'
)
layout = go.Layout(
    title='Liveness ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Liveness',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
livenessFig = go.Figure(data=[livenessData], layout=layout)
py.plot(livenessFig, filename='livenessscatter')

loudnessData = go.Scatter(
    y = peakPos,
    x = loudness,
    mode = 'markers'
)
layout = go.Layout(
    title='Loudness ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Loudness',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
loudnessFig = go.Figure(data=[loudnessData], layout=layout)
py.plot(loudnessFig, filename='loudnessscatter')

speechinessData = go.Scatter(
    y = peakPos,
    x = speechiness,
    mode = 'markers'
)
layout = go.Layout(
    title='Speechiness ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Speechiness',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
speechinessFig = go.Figure(data=[speechinessData], layout=layout)
py.plot(speechinessFig, filename='speechinessscatter')

tempoData = go.Scatter(
    y = peakPos,
    x = tempo,
    mode = 'markers'
)
layout = go.Layout(
    title='Tempo ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    Xaxis=dict(
        title='Tempo',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
tempoFig = go.Figure(data=[tempoData], layout=layout)
py.plot(tempoFig, filename='temposcatter')

time_signatureData = go.Scatter(
    y = peakPos,
    x = time_signature,
    mode = 'markers'
)
layout = go.Layout(
    title='Time Signature ScatterPlot',
    yxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Time Signature',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
time_signatureFig = go.Figure(data=[time_signatureData], layout=layout)
py.plot(time_signatureFig, filename='timesigscatter')

valenceData = go.Scatter(
    y = peakPos,
    x = valence,
    mode = 'markers'
)
layout = go.Layout(
    title='Valence ScatterPlot',
    yaxis=dict(
        title='Peak Position',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    xaxis=dict(
        title='Valence',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)
valenceFig = go.Figure(data=[valenceData], layout=layout)
py.plot(valenceFig, filename='valencescatter')