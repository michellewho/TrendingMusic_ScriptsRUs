import billboard
import pandas as pd

# Our Starting date
date = '2017-10-26'

#First billboard object with our date
chart100 = billboard.ChartData('hot-100', date)

#columns in data frame
columnList = ['Title', 'Artist', 'Rank', 'Weeks', 'PeakPos', 'Date']

#Use this to create df at end
songArray = []

#Set for unique song and artist pairings
songSet = set()

#initiate while loop (counting up days)
day = 0
while day <= 312: 
    songNum = 0
    while (songNum < 100 and chart100[songNum]):
        
        song = chart100[songNum]
        currTitle = song.title
        currArtist = song.artist
        currRank = song.rank
        currWeeks = song.weeks
        currPeakPos = song.peakPos

        #For each song we put the appropriate values into the set and array
        songSet.add((currTitle, currArtist, currPeakPos))
        songArray.append((currTitle, currArtist, currRank, currWeeks, currPeakPos, date))
        songNum += 1

    #Put our date to a day back then update our chart object to the new date
    date = chart100.previousDate
    chart100 = billboard.ChartData('hot-100', date)
    day += 1

#Create the dataframe for the general billboard and put it into a csv
songDF = pd.DataFrame(songArray, columns = columnList)
songDF.to_csv('Billboard_data_6year.csv', index=False, encoding='utf-8')

#put each object in set into an array, use this array to create df then csv
uniqueSongArray = []
for obj in songSet:
    uniqueSongArray.append(obj)
uniqueSongDF = pd.DataFrame(uniqueSongArray, columns=("SongTitle", "Artist", "Peakpos"))
uniqueSongDF.to_csv('Unique_Song_list_6year.csv', index=False, encoding='utf-8')