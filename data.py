import pandas as pd
import plotly.express as px
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('animation', html='html5')
## clean2.csv is the same as clean but places empty entries with 0s in order to compute and graph data

#clean = pd.read_csv('clean.csv')
#clean.fillna(0, inplace = True)
#clean.to_csv("clean2.csv", index = False)


clean = pd.read_csv("clean2.csv")

zips = [98106,98134,98104,98101,98109,98102,98195,98105,98115]
#ignore all this
mask = (clean['zip'].isin(zips))
year2018 = (clean['year'] == 2018)
year2019 = (clean['year'] == 2019)
year2021 = (clean['year'] == 2021)
year2022 = (clean['year'] == 2022)

q1 = (clean['legal_handheldstop'] == 1)
q2 = (clean['legal_handheldstop'] == 2)
q3 = (clean['legal_handheldstop'] == 3)
q3 = (clean['legal_handheldstop'] == 4)

x1 = clean[mask][year2018][q1]['zip'].value_counts()
x2 = clean[mask][year2019][q1]['zip'].value_counts()
x3 = clean[mask][year2021][q1]['zip'].value_counts()
x4 = clean[mask][year2022][q1]['zip'].value_counts()



y1 = clean[mask][year2018][q2]['zip'].value_counts()
y2 = clean[mask][year2019][q2]['zip'].value_counts()
y3 = clean[mask][year2021][q2]['zip'].value_counts()
y4= clean[mask][year2022][q2]['zip'].value_counts()

z1 = clean[mask][year2018][q3]['zip'].value_counts()
z2 = clean[mask][year2019][q3]['zip'].value_counts()
z3 = clean[mask][year2021][q3]['zip'].value_counts()
z4 = clean[mask][year2022][q3]['zip'].value_counts()

correct1 = y1/(x1+y1+z1)
#incorrect1 = (x1+z1)/y1

correct2 = y2/(x2+y2+z2)
#incorrect2 = (x2+z2)/y2

correct3 = y3/(x3+y3+z3)
#incorrect3 = (x3+z3)/y3

correct4 = y4/(x4+y4+z4)
#incorrect4 = (x4+z4)/y4



#this is the important stuff
#filtered everything instead of hardcoding
#function takes in df list of years and the correct answer for each question (1,2,3)
#returns line graph (need to make nicer/remove filler)
filtered_df = clean[(clean['zip'].isin(zips)) & (clean['year'] == 2018) & (clean['legal_handheldstop'] == 1)]
filtered_df = clean[(clean['zip'].isin(zips)) & (clean['year'] == 2018)]
counts = filtered_df['legal_handheldstop'].value_counts()
percentages = (counts / len(filtered_df)) * 100

def func(df,year_list,law,zips,ans): 
    percent_correct = {'year':year_list,'percentages':[]}
    for year in year_list:
        filtered_df = df[(df['zip'].isin(zips)) & (df['year'] == year)]
        val_counts = filtered_df[law].value_counts() 
        percentages = (val_counts / len(df)) * 100
        percent_correct['percentages'].append(percentages[ans])
    percent_df = pd.DataFrame(percent_correct)
    return percent_df


def scatter(df, x_ax, y_ax, title):
     fig = px.line(df, x=x_ax, y=y_ax, title=title)
     years = list(df['year'])
     x_labels = [str(year) for year in years]

     fig.update_xaxes(ticktext=x_labels)
     fig.show()


year_list = [2018, 2019, 2021, 2022]

frame = func(clean,year_list,'legal_handheldstop',zips,1)
print(frame)
scatter(frame, 'year', 'percentages', 'legal_handheldstop')





#averages from 2018,2019,2021,2022


list1 = []
for num in correct1:
    list1.append(num)
list2 = []
for num in correct2:
    list2.append(num)
list3 = []
for num in correct3:
    list3.append(num)
list4 = []
for num in correct4:
    list4.append(num)


#zips2018 = clean[clean['year'] == 2018]
#for zip in zips2018:
    #zip = clean['zip']
    #count = zip.value_counts()

#fig = px.scatter(x=years, y=correct1)
#fig.show()