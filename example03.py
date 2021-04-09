import pandas as pd
import requests as r

data = pd.read_csv('data/kc_house_data.csv')

i = 1
while True:
    print('page:{}'.format(i))
    url = 'https://www.linkedin.com/jobs/'
    response = r.request('GET',url)

    if response != []:
        data = response.text
        df = pd.DataFrame(data, index=[0])
        print(df[['id', 'type']])
        dataset = pd.concat([dataset, df], axis=0)
        i += 1
    else:
        break
