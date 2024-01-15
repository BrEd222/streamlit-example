import streamlit as st
import pandas as pd
import numpy as np
import urllib.request, json 
import requests


st.title('Test Grafico POE')
url = "https://poe.ninja/api/data/itemhistory?league=Affliction&type=UniqueFlask&itemId=20932"
data_json = requests.get(url)
#print(data_json.json())

poedf=pd.DataFrame(data_json.json())
#print(poedf['value'])
st.bar_chart(poedf['value'])




