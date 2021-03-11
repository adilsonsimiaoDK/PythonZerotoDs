import pandas as pd
data_home = pd.read_csv('dataset/kc_house_data.csv')
print(data_home.head())
data_home.date = pd.to_datetime(data_home.date)
print(data_home.dtypes)