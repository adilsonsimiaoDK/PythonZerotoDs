import pandas as pd
from geopy.geocoders import Nominatim
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import fixed

data = pd.read_csv('data/kc_house_data.csv')
data['road'] = 'NA'
data['house_number'] = 'NA'
data['city'] = 'NA'
data['county'] = 'NA'
data['state'] = 'NA'
data['neighbourhood'] = 'NA'
# geolocator = Nominatim(user_agent='geoapiExercises')
#
# # for i in range(len(data)):
# #     print('Loop:{}/{}'.format(i, len(data)))
# #
# #     query = str(data.loc[i, 'lat']) + ',' + str(data.loc[i, 'long'])
# #     response = geolocator.reverse(query)
# #
# #     if 'house_number' in response.raw['address']:
# #         data.loc[i, 'house_number'] = response.raw['address']['house_number']
# #     if 'road' in response.raw['address']:
# #         data.loc[i, 'road'] = response.raw['address']['road']
# #     if 'city' in response.raw['address']:
# #         data.loc[i, 'city'] = response.raw['address']['city']
# #     if 'county' in response.raw['address']:
# #         data.loc[i, 'county'] = response.raw['address']['county']
# #     if 'state' in response.raw['address']:
# #         data.loc[i, 'state'] = response.raw['address']['state']
# #     if 'neighbourhood' in response.raw['address']:
# #         data.loc[i, 'neighbourhood'] = response.raw['address']['neighbourhood']
#
houses = data[['id', 'long', 'lat', 'price']].copy()
for i in range(len(houses)):
    if houses.loc[i, 'price'] <= 321950:
        houses.loc[i, 'level'] = 0

    elif (houses.loc[i, 'price'] > 321950) & (houses.loc[i, 'price'] <= 450000):
        houses.loc[i, 'level'] = 1

    elif (houses.loc[i, 'price'] >= 450000) & (houses.loc[i, 'price'] <= 645000):
        houses.loc[i, 'level'] = 2

    else:
        houses.loc[i, 'level'] = 3

houses['level'] = houses['level'].astype(int)

fig = px.scatter_mapbox(houses,
                        lat='lat',
                        lon='long',
                        color='level',
                        size='price',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        size_max=20,
                        zoom=10)

fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(height=800, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
# fig.show()
df = data
df['is_waterfront'] = df['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')
df['level'] = df['price'].apply(lambda x: 0 if x < 321950 else
1 if (x > 321950) & (x < 450000) else
2 if (x > 450000) & (x < 645000) else 3)
df['level'] = df['level'].astype(int)
style = {'description_width': 'initial'}

# 3. create interactive button
price_limit = widgets.IntSlider(
    value=540000,
    min=75000,
    max=77000000,
    step=1,
    description='Maximun price',
    disable=False,
    style=style
)

waterfront_bar = widgets.Dropdown(
    options=df['is_waterfront'].unique().tolist(),
    value='yes',
    description='Water View',
    disable=False,
)


# 4. function to create the filters

def update_map(df, waterfront, limit):
    houses = df[(df['price'] <= limit) &
                (df['is_waterfront'] == waterfront)][['id', 'lat', 'long', 'price', 'level']]

    # 5. Map plot
    fig = px.scatter_mapbox(houses,
                            lat='lat',
                            lon='long',
                            color='level',
                            size='price',
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=800, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    fig.show()


# 5. iteration
widgets.interactive(update_map, df=fixed(df), waterfront=waterfront_bar, limit=price_limit)

