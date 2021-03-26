import pandas as pd
data = pd.read_csv('data/kc_house_data.csv')
# showing the types of variables
print(data.dtypes)
# First step to check and convert the variables to type necessary
data['date'] = pd.to_datetime(data['date'])
data['bedrooms']= data['bedrooms'].astype('float')
print(data.dtypes)