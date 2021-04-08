import pandas as pd
import requests as r

data = pd.read_csv('data/kc_house_data.csv')
url = 'https://www.linkedin.com/jobs/'
response = r.request('GET',url)
print(response.json())
