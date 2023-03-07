import pandas as pd
import plotly.express as px

zips = [98105,98101,98102,98115,98106]

clean = pd.read_csv('clean.csv')

mask = (clean['zip'].isin(zips))
mask2 = clean['legal_911'] == 1

print(clean[mask][mask2]['legal_911'].value_counts())
print(clean[mask]['legal_911'].value_counts())