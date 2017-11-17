import pandas as pd

peakPosArray = []

billBoard_1yr = pd.read_csv('Billboard_data.csv')
unique_1yr = pd.read_csv('Unique_Song_list.csv')

peakpos = 0
innerloop = True
for index, row in unique_1yr.iterrows():
    
    songU = row['SongTitle']
    
    for index1, row1 in billBoard_1yr.iterrows():
        while(innerloop) :
            if (songU == row1['Title']):
                peakpos = row1['PeakPos']
                innerloop = False
    peakPosArray.append((row['SongTitle'], row['Artist'], peakpos))
    peakpos = 0
    innerloop = True

columnList = ('SongTitle', 'Title', 'PeakPos')
uSongDF = pd.DataFrame(peakPosArray, columns = columnList)
uSongDF.to_csv('unique_song_peakPos_6yr.csv', index= False, encoding='utf-8')
