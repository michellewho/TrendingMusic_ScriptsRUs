import pandas as pd

peakPosArray = []

billBoard = pd.read_csv('../data/Billboard_data.csv')
unique = pd.read_csv('../data/Unique_Song_list.csv')

peakPos = 0

for index, row in unique.iterrows(): 

    songU = row['SongTitle']
    rowSongTitle = row['SongTitle']
    rowArtist = row['Artist']

    for index1, row1 in billBoard.iterrows(): 
        
        rowTitle = row1['Title']
        rowPeakPos = row1['PeakPos']


        if (songU == rowTitle): 
            if(rowPeakPos > peakPos):
                peakPos = rowPeakPos
    peakPosArray.append((rowSongTitle, rowArtist, peakPos))
    peakPos = 0

columnList = ('SongTitle', 'Title', 'PeakPos')
uSongDF = pd.DataFrame(peakPosArray, columns=columnList)
uSongDF.to_csv('unique_song_peakPos_6yr.csv', index=False, encoding='utf-8')