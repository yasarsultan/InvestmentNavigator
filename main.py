import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def commodities(period):
    gold = pd.read_csv('data/gold.csv', index_col='Date')
    gold.index = pd.to_datetime(gold.index)
    last_date = gold.index[-1]
    if period == 1:
        one_year_ago = last_date - pd.DateOffset(years=1)
        actual_date = gold.index.searchsorted(one_year_ago)
        gold = gold.iloc[actual_date:]
    elif period == 5:
        five_years_ago = last_date - pd.DateOffset(years=5)
        actual_date = gold.index.searchsorted(five_years_ago)
        gold = gold.iloc[actual_date:]
    else:
        pass
    gold.loc[:, 'Cumulative Returns'] = gold['Change'].cumsum()
    
    return gold[['Cumulative Returns']]


def real_estate(period):
    public = pd.read_csv('data/realEstate.csv', names=['Date', 'returns'], skiprows=1, index_col='Date')
    public.index = pd.to_datetime(public.index)
    last_date = public.index[-1]
    if period == 1:
        one_year_ago = last_date - pd.DateOffset(years=1)
        actual_date = public.index.searchsorted(one_year_ago)
        public = public.iloc[actual_date:]
    elif period == 5:
        five_years_ago = last_date - pd.DateOffset(years=5)
        actual_date = public.index.searchsorted(five_years_ago)
        public = public.iloc[actual_date:]
    else:
        ten_years_ago = last_date - pd.DateOffset(years=10)
        actual_date = public.index.searchsorted(ten_years_ago)
        public = public.iloc[actual_date:]
    public.loc[:, 'Cumulative Returns'] = public['returns'].cumsum()

    return public[['returns', 'Cumulative Returns']]


def securities(period):
    bonds = pd.read_csv('data/bonds.csv', index_col=0)
    years = [0]
    if period == 1:
        bond = bonds.loc[0, '1yBond']
    elif period == 5:
        bond = bonds.loc[0, '5yBond']
    else:
        bond = bonds.loc[0, '10yBond']
    for _ in range(period):
        years.append(bond + years[-1])

    return years


def equities(period, index='nifty50'):
    data = None
    if index == 'nifty50':
        nifty50 = pd.read_csv('data/nifty50.csv', index_col='Date')
        nifty50.index = pd.to_datetime(nifty50.index)
        last_date = nifty50.index[-1]
        if period == 1:
            one_year_ago = last_date - pd.DateOffset(years=1)
            actual_date = nifty50.index.searchsorted(one_year_ago)
            nifty50 = nifty50.iloc[actual_date:]
        elif period == 5:
            five_years_ago = last_date - pd.DateOffset(years=5)
            actual_date = nifty50.index.searchsorted(five_years_ago)
            nifty50 = nifty50.iloc[actual_date:]
        else:
            pass
        nifty50.loc[:, 'Cumulative Returns'] = nifty50['Change'].cumsum()
        data = nifty50

    elif index == 'sensex':
        sensex = pd.read_csv('data/sensex.csv', index_col='Date')
        sensex.index = pd.to_datetime(sensex.index)
        last_date = sensex.index[-1]
        if period == 1:
            one_year_ago = last_date - pd.DateOffset(years=1)
            actual_date = sensex.index.searchsorted(one_year_ago)
            sensex = sensex.iloc[actual_date:]
        elif period == 5:
            five_years_ago = last_date - pd.DateOffset(years=5)
            actual_date = sensex.index.searchsorted(five_years_ago)
            sensex = sensex.iloc[actual_date:]
        else:
            pass
        sensex.loc[:, 'Cumulative Returns'] = sensex['Change'].cumsum()
        data = sensex
        
    return data[['Cumulative Returns']]



def crypto(period):
    bitcoin = pd.read_csv('data/bitcoin.csv', index_col='Date')
    bitcoin.index = pd.to_datetime(bitcoin.index)
    last_date = bitcoin.index[-1]
    if period == 1:
        one_year_ago = last_date - pd.DateOffset(years=1)
        actual_date = bitcoin.index.searchsorted(one_year_ago)
        bitcoin = bitcoin.iloc[actual_date:]
    elif period == 5:
        five_years_ago = last_date - pd.DateOffset(years=5)
        actual_date = bitcoin.index.searchsorted(five_years_ago)
        bitcoin = bitcoin.iloc[actual_date:]
    else:
        pass
    bitcoin.loc[:, 'Cumulative Returns'] = bitcoin['Change'].cumsum()
    
    return bitcoin[['Cumulative Returns']]
