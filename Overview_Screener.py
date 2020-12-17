import os
import webbrowser

#data scrapping efforts failed
import urllib.request



def overview_screener():


    ticker = input("Please enter the stock ticker for screening: ")

    prefix_screener = 'https://finviz.com/quote.ashx?t='
    togo_screener = prefix_screener + ticker

    print("You are directed to: " + togo_screener)


    webbrowser.open(togo_screener)


overview_screener()






    





    #from yahoo_finance import Share 
    #aapl = Share('YHOO')
    #print(aapl)


