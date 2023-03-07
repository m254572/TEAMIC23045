import pandas as pd
import plotly.express as px

"""
every question
"""

#use the same five zipcodes
zips = [98106,98134,98104,98101,98109,98102,98195,98105,98115]
years = [2018,2019,2021,2022]
iquestions = ['legal_addgps','legal_handheld','legal_handheldstop','legal_camera','legal_music1819','legal_readstop','legal_typestop','legal_app1819','legal_video','legal_gps2122','legal_music2122','legal_app2122']
lquestions = ['legal_gps1819','legal_911','legal_handfree']

# read in the file
clean = pd.read_csv('clean.csv')

#dataframe mask for the zipcodes AND correct answer(in this case, the correct answer is legal)
mask = (clean['zip'].isin(zips))
maskn = (~clean['zip'].isin(zips))

#Legals
for q in lquestions:
    mask2 = clean[q] == 1
    datad = []
    for year in years:
        y = (clean['year'] == year)

        # % correct inside the train district
        cort = int(clean[mask][y][mask2][q].dropna().count())/(clean[y][mask].shape[0])

        # % correct outside of the train district
        corn = int(clean[maskn][y][mask2][q].dropna().count())/(clean[y][maskn].shape[0])

        datad.append([year,cort,corn])
    df = pd.DataFrame(datad, columns=['Year', '% Correct close to train', '% Correct away from train'])

    fig = px.line(df, x='Year',
                y=['% Correct close to train', '% Correct away from train'],
                title=(f'{q}'),
                labels={
                        "value":'% Correct',
                        "variable":'Key'
                        }
                )
    fig.show()

#Illegals
for q in iquestions:
    mask2 = clean[q] == 2
    datad = []
    for year in years:
        y = (clean['year'] == year)

        # % correct inside the train district
        cort = int(clean[mask][y][mask2][q].dropna().count())/(clean[y][mask].shape[0])

        # % correct outside of the train district
        corn = int(clean[maskn][y][mask2][q].dropna().count())/(clean[y][maskn].shape[0])

        datad.append([year,cort,corn])
    df = pd.DataFrame(datad, columns=['Year', '% Correct close to train', '% Correct away from train'])

    fig = px.line(df, x='Year',
                y=['% Correct close to train', '% Correct away from train'],
                title=(f'{q}'),
                labels={
                        "value":'% Correct',
                        "variable":'Key'
                        }
                )
    fig.show()