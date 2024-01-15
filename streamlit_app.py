import streamlit as st
import pandas as pd
import numpy as np
import urllib.request, json 
import requests
from pandas import json_normalize


@st.cache_data
def get_ninja(url):
    data_json = requests.get(url)
    pd_json = json_normalize(data_json,record_path='lines')    
    return data


st.title('Test Grafico POE')

url = "https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency"
r = requests.get(url)
curr_list = get_ninja(url)
#print(data_json)

curr_list = json_normalize(curr_list,record_path='lines')

selection = st.selectbox('Select', curr_list['currencyTypeName'].values)
#st.text([selection])

#id=pd_json[pd_json['currencyTypeName']==selection]['pay.pay_currency_id'].values[0]
#ids=str(int(id))

#url_history = 'https://poe.ninja/api/data/currencyhistory?league=Affliction&type=Currency&currencyId='+ids

#curr_hist = get_ninja(url_history)

#url = "https://poe.ninja/api/data/itemhistory?league=Affliction&type=UniqueFlask&itemId=20932"

#Currency overview
#https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency

#Currency history
#https://poe.ninja/api/data/currencyhistory?league=Affliction&type=Currency&currencyId=22

#st.bar_chart(curr_hist['value'])