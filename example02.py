import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import gridspec
import plotly.express as px
pd.set_option('display.float_format', lambda x: '%.2f' % x)
data = pd.read_csv('data/kc_house_data.csv')
data['dormitory_type'] = 'properties'
data.loc[data['bedrooms'] < 1, 'dormitory_type'] = 'business_point'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'
# Groupby: split, apply, combine
# df_group = data[['id', 'bedrooms', 'price']].groupby('bedrooms')
# for bedrooms, frame in df_group:
#     print(f' number of bedroom {bedrooms}')
#     print(frame.head(), end='\n' )
# 1. Number of properties for year of built.
# print(data[['id', 'yr_built','price' ]].groupby('yr_built').count())
# 2. How many small bedroom has for year of build.
# print(data[['bedrooms', 'yr_built']].groupby('yr_built').min())
# 3. What is pricer for number of bedrooms
# print(data[['price', 'bedrooms']].groupby('price').max())
# 4.what is sum total of houses for number of bedrooms
# print(data[['price', 'bedrooms']].groupby('bedrooms').sum())
# 5. what is sum of all the prices for number of bedrooms and bathrooms
# print(data[['price', 'bedrooms', 'bathrooms']].groupby(['bedrooms', 'bathrooms']).sum())
# 6. what is mean size of living_rooms and year of build
# print(data[['sqft_living', 'yr_built']].groupby('yr_built').mean())
# 7.
# print(data[['sqft_living', 'yr_built']].groupby('yr_built').median())
# 8.
# print(data[['sqft_living', 'yr_built']].groupby('yr_built').std())
# 9. How is the Average price growth of the properties for year, week and day?
data['date'] = pd.to_datetime(data['date'])
fig = plt.figure(figsize=(20, 12))
specs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig)
ax1 = fig.add_subplot(specs[0, :])
ax2 = fig.add_subplot(specs[1, 0])
ax3 = fig.add_subplot(specs[2, 0])
# 1. ============================================
data['year'] = pd.to_datetime(data['date']).dt.year
by_year = data[['price', 'year']].groupby('year').sum().reset_index()
ax1.bar(by_year['year'], by_year['price'])
# 2. =============================================
data['day'] = pd.to_datetime(data['date'].dt.day)
by_day = data[['price', 'day']].groupby('day').mean().reset_index()
ax2.plot(by_day['day'], by_day['price'])
# 3.==============================================
data['week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
by_week = data[['price', 'week']].groupby('week').mean().reset_index()
ax3.plot(by_week['week'], by_week['price'])
plt.xticks(rotation=60)
# plt.show()
# ===============================================
# maps identify of the houses high price
houses = data[['id', 'lat', 'long', 'price']]
fig = px.scatter_mapbox(houses, lat='lat',
                        lon='long',
                        size='price',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        size_max=15,
                        zoom=10)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(height=1020, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
# fig.show()
# graphs
rooms1 = data[['price', 'bedrooms']].groupby('bedrooms').sum().reset_index()
rooms2 = data[['price', 'yr_built']].groupby('yr_built').mean().reset_index()
rooms3 = data[['price', 'dormitory_type']].groupby('dormitory_type').mean().reset_index()
# rooms4 = data[['price', 'yr_renovated']].groupby(['yr_renovated'] > 1930).mean().reset_index()
rooms4 = data[((data['price'] > 0) & (data['yr_renovated'] > 1930).mean())]
# plt.bar(rooms1['bedrooms'], rooms1['price'])
# plt.plot(rooms2['yr_built'], rooms2['price'])
# plt.bar(rooms3['dormitory_type'], rooms3['price'])
plt.bar(rooms4['dormitory_type'], rooms4['price'])
# plt.show()
