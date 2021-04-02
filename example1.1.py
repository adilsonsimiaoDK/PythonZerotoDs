import pandas as pd
import plotly.express as px

data = pd.read_csv('data/kc_house_data.csv')
# showing the types of variables
# First step to check and convert the variables to type necessary

data['date'] = pd.to_datetime(data['date'])
data['bedrooms'] = data['bedrooms'].astype('int')
data['yr_built'] = pd.to_datetime(data['yr_built'])
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])

# print(data.dtypes)
# =====================================================
# creating new variables and columns
data['house_age'] ='new'
data['house_age'] = data['house_age'].astype('str')

data.loc[data['date'] > '2015-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2015-01-01', 'house_age'] = 'old_house'
data['dormitory_type']='type'
data['dormitory_type'] = data['dormitory_type'].astype('str')
data.loc[data['bedrooms'] < 1, 'dormitory_type'] = 'business_point'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'
# print(data.loc[data['dormitory_type'] == 'business_point'] )
data['condition_type'] = 'regular'
data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'] == 4, 'condition_type'] = 'regular'
data.loc[data['condition'] >= 5, 'condition_type'] = 'good'
data['condition'] = data['condition'].astype(str)
# =====================================================
# delete a variables
cols_del = data[['sqft_living15','sqft_lot15']]
data = data.drop(cols_del, axis=1)
# =======================================================
# date of the properties eldest and newest
# print(data.sort_values('date', ascending=True))
# print(data.sort_values('date', ascending=False))
# ===========================================
# select data by index with iloc quantity rows 0:n, quantity columns 0:n
# print(data.loc[data['floors'] == 2].shape)
# print(data.loc[data['condition_type'] == 'regular'].shape)
# print(data[((data['house_age'] == 'new_house') & (data['condition_type'] == 'good'))])
# print(data[((data['condition_type'] == 'bad') & (data['waterfront'] == 1))])
# print(data[['condition_type', 'price']].loc[data['dormitory_type'] == 'studio'].sort_values('price', ascending=False))
# print(data[((data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == 2015).shape)])
# print(data[['dormitory_type','bedrooms']].loc[data['dormitory_type']=='house'].sort_values('bedrooms',ascending=False))
# print(data[(data['house_age']=='new_house') & (data['yr_renovated']=='2014')].shape)
# print(data[['id', 'date', 'price', 'floors', 'zipcode']])
# print(data.iloc[:,[0,1,2, 7, 16]])
# col = data[['id', 'date', 'price', 'floors', 'zipcode']]
# print(data.loc[0:5, col])
# print(data.shape)
# cols=[True,True,True,False,False,False,False,
#         True,False,False,False,False,False,False,False,
#         False,True,False,False,False,False,False]
# print(data.loc[:, cols])

# ========================================================
# select data by index and columns name with loq quantity rows 0:n qat col 0:name
# print(data.loc[0:3, 'price'])
# ============ select data by boolean ===============
# print(data.shape)
# cols = ['True', 'False', 'True', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
#         'False',
#         'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False']
# print(data.loc[0:10, cols])


# ===============================================
# A report of houses sorted by prices
report = data[['id', 'date', 'price', 'floors', 'zipcode']].sort_values('price', ascending=False)
report.to_csv('data/report1.1.csv', index=False)
# print(report.head())
# ==============================================
# libraries that drawing maps Plotly
data_maps = data[['id','lat', 'long', 'price']]
mapss = px.scatter_mapbox(data_maps, lat='lat', lon='long',
                          hover_name='id',
                          hover_data=['price'],
                          color_discrete_sequence=['pink'], zoom=6, height=300)
mapss.update_layout(mapbox_style='open-street-map')
mapss.update_layout(height=1080, margin={'r':0, 't':0, 'l':0, 'b':0})
mapss.show()
# mapss.write_html('data/map_house.html')