import streamlit as st
import pandas as pd
import numpy as np
import urllib.request, json 
import requests
from pandas import json_normalize


@st.cache_data
def get_ninja(url):
    r = requests.get(url)
    pd_json = json_normalize(r.json(),record_path='lines')  
    return pd_json

@st.cache_data
def ninja_cur_hist(url):
    r = requests.get(url)
    pd_json = json_normalize(r.json(),record_path='receiveCurrencyGraphData')    
    return pd_json

st.title('Test Grafico POE')

url = "https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency"
curr_list = get_ninja(url)
#print(data_json)

selection = st.selectbox('Currency', curr_list['currencyTypeName'].values)
#st.text([selection])

id=curr_list[curr_list['currencyTypeName']==selection]['pay.pay_currency_id'].values[0]
ids=str(int(id))
st.text(ids)

url_history = 'https://poe.ninja/api/data/currencyhistory?league=Affliction&type=Currency&currencyId='+ids

curr_hist = ninja_cur_hist(url_history)
#st.bar_chart(curr_hist['value'])
st.line_chart(curr_hist['value'])#,x="Chaos Equivalent",y="Giorno di Lega")


st.vega_lite_chart(
   curr_hist.drop['count'],
   {
       "mark": {"type": "line","interpolate": "step-after", "tooltip": True},
       "encoding": {
           "x": {"field": "Giorni di Lega", "type": "quantitative"},
           "y": {"field": "Chaos Equivalent", "type": "quantitative"},
       },
   },
)

#url = "https://poe.ninja/api/data/itemhistory?league=Affliction&type=UniqueFlask&itemId=20932"

#Currency overview
#https://poe.ninja/api/data/currencyoverview?league=Affliction&type=Currency

#Currency history
#https://poe.ninja/api/data/currencyhistory?league=Affliction&type=Currency&currencyId=22

