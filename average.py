''' Produces a graph for the percentage of "legal" responses vs. year for all of King County
'''

import pandas as pd
import plotly.express as px

"""
Is calling 911 when you are driving LEGAL or ILLEGAL?
LEGAL!
"""

# #use the same five zipcodes
# zips = [98106,98134,98104,98101,98109,98102,98195,98105,98115]
years = [2018,2019,2021,2022]

# read in the file
clean = pd.read_csv('clean.csv')


# Counts totals for each year
all_county = pd.DataFrame()
all_county['counts']= clean.value_counts(normalize=False, subset='year')


# print(all_county)


# dataframe mask for the zipcodes AND correct answer(in this case, the correct answer is legal)
mask2 = (clean['legal_911'] == 1)


datad = []

for year in years:
    y = (clean['year'] == year)

    # % correct 
    correct = int(clean[mask2]['legal_911'].value_counts())#/(all_county['counts'])
    c = clean[y][mask2]['legal_911'].value_counts()
    num = int(clean[mask2]['legal_911'].value_counts())
    # print(c)
    # print(num)
    datad.append([year,c])

# print(datad)

df = pd.DataFrame(datad, columns=['Year', '% Correct'])
print(df)


# fig = px.line(df, x='Year',
#               y=['% Correct']
#               title='Is it legal to call 911 when driving?',
#               labels={
#                       "value":'% Correct',
#                       "variable":'Key'
#                      }
#               )
# fig.show()
