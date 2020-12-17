import os
#from menus import lst_tickers
#import textwrap

#wrapper = 

def Parameters_Entry():

    about_financials = " \n"\
                       "1. Enter Market Cap (in $million): \n"\
                       "2. Enter Current Ratio: \n"\
                       "3. Enter Debt/Equity Ratio: \n"\
                       "4. Enter P/E Ratio: \n"\
                       "5. Enter Alpha: \n"\
                       "6. Enter Sharpe Ratio: \n"\
                       "7. Enter Info Ratio: \n"\
                       "9. Enter 95% VaR: \n"\
                        
                            
    about_Rates = "9.  Enter Credit_Rate(Note: if the ticker represents an ETF fund or a index, assign highest soverign credit rating for that jurisdiction ): \n"\
                  "10.  Enter Industry Life Cycle(Note: 1.5 for growth, 2.5 for startups, 1 for maturity, 2 for shakeout, and 1.5 for decline): \n"\
                  "11. Enter MStar_Rate(5 stars for 5): \n"\
                  "12. Enter Select Experts' Rate on the underlying company's vision and its potential to achieve and gain from its visions: \n"\
                  "13. Enter Select Experts' Average Rating on the company\n"\


    print(about_financials)
    print(about_Rates)

    ticker = input("Enter ticker to enter parameters: ")

    #try exception:     length of the list
    #try exception:     int/str of each of the parameters

    ticker1_entry = input("Please enter parameters for " + ticker)

    
    ticker1_parameters = ticker1_entry.split()

    print("the value of the parameters are: ")
    print(ticker1_parameters)
    return ticker1_parameters,ticker


Parameters_Entry()

'''
        
    elif len(lst_tickers) ==2:
        
        print(about_financials)
        print(about_Rates)
        ticker = input("Enter ticker to enter parameters: ")
        ticker1_entry = input("Please enter parameters for " + lst_tickers[0])
        ticker1_entry.split()
        
        ticker2_entry = input("Please enter parameters for " + lst_tickers[1])
        ticker2_entry.split()        
        
            
    elif len(lst_tickers) ==3:
        
        print(about_financials)
        print(about_Rates)
        
        ticker1_entry = input("Please enter parameters for " + lst_tickers[0])
        ticker1_entry.split()
        
        ticker2_entry = input("Please enter parameters for " + lst_tickers[1])
        ticker2_entry.split()        
        
        ticker3_entry = input("Please enter parameters for " + lst_tickers[2])
        ticker3_entry.split()   



    elif len(lst_tickers) ==4:
        
        print(about_financials)
        print(about_Rates)
        
        ticker1_entry = input("Please enter parameters for " + lst_tickers[0])
        ticker1_entry.split()
        
        ticker2_entry = input("Please enter parameters for " + lst_tickers[1])
        ticker2_entry.split()        
        
        ticker3_entry = input("Please enter parameters for " + lst_tickers[2])
        ticker3_entry.split()   

        ticker4_entry = input("Please enter parameters for " + lst_tickers[3])
        ticker4_entry.split()   


    elif len(lst_tickers) ==5:
        
        print(about_financials)
        print(about_Rates)
        
        ticker1_entry = input("Please enter parameters for " + lst_tickers[0])
        ticker1_entry.split()
        
        ticker2_entry = input("Please enter parameters for " + lst_tickers[1])
        ticker2_entry.split()        
        
        ticker3_entry = input("Please enter parameters for " + lst_tickers[2])
        ticker3_entry.split()   

        ticker4_entry = input("Please enter parameters for " + lst_tickers[3])
        ticker4_entry.split()   

        ticker5_entry = input("Please enter parameters for " + lst_tickers[4])
        ticker5_entry.split()   


Parameters_Entry()

'''





















