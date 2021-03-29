import pandas as pd
import plotly.express as px

data = pd.read_csv('data/kc_house_data.csv')
# showing the types of variables
# First step to check and convert the variables to type necessary
data['date'] = pd.to_datetime(data['date'])
data['bedrooms'] = data['bedrooms'].astype('int')
# =====================================================
# creating new variables
data['date_new_home'] = pd.to_datetime('2021-03-29')
data['price_high'] = data['price'].max()
# =====================================================
# delete a variables
# data = data.drop('date_new_home', axis=1)
# delete more than one variables
col = data[['date_new_home', 'price_high']]
data = data.drop(col, axis=1)
cols = ['True', 'False', 'True', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
        'False',
        'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False']
# =======================================================
# select data by index with iloc quantity rows 0:n, quantity columns 0:n
# print(data.iloc[0:10, 0:])
# ========================================================
# select data by index and columns name with loq quantity rows 0:n qat col 0:name
# print(data.loc[0:3, 'price'])
# ============ select data by boolean ===============
# print(data.shape)
# print(data.loc[0:10, cols])
# ===========================================
# date of the properties eldest and newest
# print(data['date'].min())
# print(data['date'].max())
# print(data.sort_values('date', ascending=True))
# ============================================
# How many properties and o max number of the rooms
# print(data[data['floors'] == 3.5][['id', 'floors']])
# print(data[data['floors'] == 3.5].shape)
# ==============================================
# created columns level, select high and small price after that classification the home
data['level'] = 'standard'
data.loc[data['price'] > 540000, 'level'] = 'high_standard'
data.loc[data['price'] < 540000, 'level'] = 'low_standard'
# print(data.sort_values('price', ascending=False))
# ===============================================
# A report of houses sorted by prices
report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price', ascending=False)
report.to_csv('data/report01.csv', index=False)
print(report.head())
# ==============================================
# libraries that drawing maps Plotly
data_maps = data[['id','lat', 'long', 'price']]
mapss = px.scatter_mapbox(data_maps, lat='lat', lon='long',
                          hover_name='id',
                          hover_data=['price'],
                          color_discrete_sequence=['orange'], zoom=6, height=300)
mapss.update_layout(mapbox_style='open-street-map')
mapss.update_layout(height=1080, margin={'r':0, 't':0, 'l':0, 'b':0})
mapss.show()
mapss.write_html('data/map_house.html')