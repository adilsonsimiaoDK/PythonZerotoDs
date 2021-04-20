import pandas as pd
import streamlit as st

st.title('House Rocket Company')
st.markdown('Welcome to House Rocket Data')
st.header('Load data')


@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data


# load data
data = get_data('data/kc_house_data.csv')

st.dataframe(data.head())
# filter bedrooms
bedrooms = st.sidebar.multiselect('Number of Bedrooms', data['bedrooms'].unique())
st.write('You chosen', bedrooms[0])