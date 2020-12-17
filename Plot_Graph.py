
import numpy as np
import pandas as pd

from datetime import datetime
from pandas_datareader import data
#no matching distribution
#from pandas_datareader._ultils import RemoteDataError

import matplotlib.pyplot as plt

# # # What to do to receive values of lst_tickers from menus,py?
# # # Or say, how to receive values of a global variable from another .py file?

### Can be expanded to take over 2 tickers for comparison

'''
from menu0 import lst_tickers
lst_stickers = menus.ticker_input.lst_tickers
print(lst_stickers[0])
'''


ticker = input("Please enter the first stock ticker for Historical Returns Graphing: ")
ticker2 = input("Please enter the second stock ticker for Historical Returns Graphing: ")



START_DATE = '2015-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

STOCK_A = str(ticker).upper()
STOCK_B = str(ticker2).upper()



def get_stats(stock_data):
    return {
        'last':np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(30)),
        'long_mean': np.mean(stock_data.tail(90)),
        'short_rolling': stock_data.rolling(window=30).mean(),
        'long_rolling': stock_data.rolling(window=90).mean(),

        }


def clean_data(stock_data, col):
    weekdays = pd.date_range(start = START_DATE, end = END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method = 'ffill')

def create_plot(stock_data,stock_data2, ticker1,ticker2):
    
        plt.style.use('dark_background')
        stats = get_stats(stock_data)
        stats2 = get_stats(stock_data2)
        
        plt.subplots(figsize = (12, 8))
    
        plt.plot(stock_data, label = ticker1 + ' Daily Adj Close')
        plt.plot(stats['short_rolling'], label = '30 Day Rolling Mean')
        plt.plot(stats['long_rolling'], label = '90 Day Rolling Mean')
        
        plt.plot(stock_data2, label = ticker2 + ' Daily Adj Close')
        plt.plot(stats2['short_rolling'], label = '30 Day Rolling Mean')
        plt.plot(stats2['long_rolling'], label = '90 Day Rolling Mean')
    
        plt.xlabel('Date')
        plt.ylabel('Adj Close)')
        plt.legend()
        plt.title(ticker + ' vs ' + ticker2 + ' Stock Price over Time')
        plt.show()
        

def get_data(ticker):
    
    #try:
        stock_data = data.DataReader(ticker,
                                     'yahoo',
                                     START_DATE,
                                     END_DATE)

        stock_data2 = data.DataReader(ticker2,
                                      'yahoo',
                                      START_DATE,
                                      END_DATE)
        
        adj_close = clean_data(stock_data,'Adj Close')
        adj_close2 = clean_data(stock_data2,'Adj Close')



        create_plot(adj_close, adj_close2, ticker, ticker2)

get_data(ticker)
        
        
    #except: RemoteDataError:
       # print('No data found for {t}'.format(t=ticker))

#get_data(STOCK_A)

#get_data(STOCK_B)


















