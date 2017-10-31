import billboard
import pandas as pd

# we need to figure out what the difference is and choose one 
chart200 = billboard.ChartData('billboard-200')
chart100 = billboard.ChartData('hot-100')

columns = ['Title', 'Artist', 'Rank', 'Weeks', 'PeakPos']

week = 0
while week <= 2: 
    songNum = 0
    while songNum <= 100:
        song = chart100[0]
        
        currTitle = song.title
        currArtist = song.artist
        currRank = song.rank
        currWeeks = song.weeks
        currPeakpos = song.peakPos

        songNum = songNum + 1

    chart100 = billboard.ChartData('hot-100', chart100.previousDate)
    week = week + 1

