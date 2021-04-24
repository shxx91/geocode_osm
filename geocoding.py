import pandas as pd
import geopandas as gpd
import numpy as np
import json
import folium
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy import distance

df = pd.read_csv('dir-arquivo-aqui', encoding='UTF8')

df['Street Number'] = df['Street Number'].astype(str)

df['Full Address'] = df['Street Number'] + str(', ') + df['Street Name'] + str(', ') + df['Zipcode'] + str(', ') + df['City'] + str(', ') + df['State']+ str(', ') + df['Country']

geocoder = RateLimiter(Nominatim(user_agent='user290').geocode, min_delay_seconds=1)
df['Location'] = df['Full Address'].apply(geocoder)

df['Latitude'] = df['Location'].apply(lambda loc: loc.latitude if loc else None)
df['Longitude'] = df['Location'].apply(lambda loc: loc.longitude if loc else None)

df.to_csv('dir-arquivo-aqui', encoding='UTF8')

#dropar as nans pra plotar no mapa
df = df.dropna(subset=['Longitude'])
df = df.dropna(subset=['Latitude'])

for i in range(0,len(df)):
   folium.Marker(
      location=[df.iloc[i]['Latitude'], df.iloc[i]['Longitude']],
      popup=df.iloc[i]['Full Address'],
   ).add_to(m)

m




