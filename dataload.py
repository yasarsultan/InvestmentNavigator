import requests 
import os 
import pandas as pd 
import yfinance as yf 
from fredapi import Fred 


def load_gold():
    gold_data = yf.download('GOLDBEES.NS', period='10y')
    gold_data['Change'] = gold_data['Close'].pct_change().fillna(0)
    gold = gold_data[['Close', 'Change']]
    gold.to_csv('data/gold.csv')

def load_realEstate():
    fred = Fred()
    data = fred.get_series('QINN628BIS', units='pch').fillna(0)
    real_estate = data.to_frame('returns')
    real_estate.to_csv('data/realEstate.csv')

def load_securities(): 
    api_key = os.environ.get('EOD_API_KEY')
    url = f'https://eodhd.com/api/eod/IN10Y.GBOND?filter=last_close&api_token={api_key}&fmt=json'
    bond_data10y = requests.get(url).json()
    url = f'https://eodhd.com/api/eod/IN5Y.GBOND?filter=last_close&api_token={api_key}&fmt=json'
    bond_data5y = requests.get(url).json()
    url = f'https://eodhd.com/api/eod/IN1Y.GBOND?filter=last_close&api_token={api_key}&fmt=json'
    bond_data1y = requests.get(url).json()
    bond_data = pd.DataFrame()
    bond_data['10yBond'] = [bond_data10y]
    bond_data['5yBond'] = [bond_data5y]
    bond_data['1yBond'] = [bond_data1y]
    bond_data.to_csv('data/bonds.csv')


def load_equities():
    nifty50 = yf.download('^NSEI', period='10y')
    nifty50['Change'] = nifty50['Close'].pct_change().fillna(0)
    nifty = nifty50[['Close', 'Change']]

    sensex = yf.download('^BSESN', period='10y')
    sensex['Change'] = sensex['Close'].pct_change().fillna(0)
    sensex = sensex[['Close', 'Change']]

    nifty.to_csv('data/nifty50.csv')
    sensex.to_csv('data/sensex.csv')

def load_crypto():
    bitcoin = yf.download('BTC-INR', period='10y')
    bitcoin['Change'] = bitcoin['Close'].pct_change().fillna(0)
    bitcoin = bitcoin[['Close', 'Change']]

    bitcoin.to_csv('data/bitcoin.csv')

