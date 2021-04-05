import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x)

data = pd.read_csv('data/kc_house_data.csv')
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
print(data[['sqft_living', 'yr_built']].groupby('yr_built').median())

