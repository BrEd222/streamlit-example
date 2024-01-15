import streamlit as st
import pandas as pd
import numpy as np
import urllib.request, json 
import requests
from pandas import json_normalize



st.title('Test Grafico POE')
url = "https://poe.ninja/api/data/itemhistory?league=Affliction&type=UniqueFlask&itemId=20932"
data_json = requests.get(url)

poedf=pd.DataFrame(data_json.json())
#print(poedf['value'])
st.bar_chart(poedf['value'])

url = "https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency"
r = requests.get(url)
data_json = r.json()
#print(data_json)

pd_json = json_normalize(data_json,record_path='lines')

st.selectbox('Select', [1,2,3])
