import pandas as pd
import plotly.express as px

"""
Is calling 911 when you are driving LEGAL or ILLEGAL?
LEGAL!
"""

#use the same five zipcodes
zips = [98106,98134,98104,98101,98109,98102,98195,98105,98115]
years = [2018,2019,2021,2022]

# read in the file
clean = pd.read_csv('clean.csv')

q = 'legal_911'
#dataframe mask for the zipcodes AND correct answer(in this case, the correct answer is legal)
mask = (clean['zip'].isin(zips))
maskn = (~clean['zip'].isin(zips))
mask2 = clean[q] == 1


datad = []
for year in years:
    y = (clean['year'] == year)

    # % correct inside the train district
    cort = int(clean[mask][y][mask2][q].value_counts())/(clean[y][mask].shape[0])

    # % correct outside of the train district
    corn = int(clean[maskn][y][mask2][q].value_counts())/(clean[y][maskn].shape[0])

    datad.append([year,cort,corn])

# print(datad)

df = pd.DataFrame(datad, columns=['Year', '% Correct close to train', '% Correct away from train'])
# print(df)


fig = px.line(df, x='Year',
              y=['% Correct close to train', '% Correct away from train'],
              title='Is it legal to call 911 when driving?',
              labels={
                      "value":'% Correct',
                      "variable":'Key'
                     }
              )
fig.show()