import pandas as pd
import requests
import simplejson as json
from datetime import datetime, date

def get_data(ticker):
    url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json'
    params = {'api_key':'FDNX5xQ2BK_8rbBuwn16', 'qopts.columns':'date,close'}
    params['ticker'] = ticker
    
    end_date = date.today()
    start_date = end_date.replace(year = end_date.year if end_date.month > 1 else end_date.year - 1, month = end_date.month - 1 if end_date.month > 1 else 12)
    
    response = requests.get(url,params)
    json = response.json()
    data = json['datatable']['data']
    df = pd.DataFrame(data)
    try:
        df = df.set_index(0)
        df.index = pd.to_datetime(df.index)
        df.columns = ['closing']
        df = df.sort_index()
        return df[start_date:end_date]
    except Exception as e:
        df = []
        return df
