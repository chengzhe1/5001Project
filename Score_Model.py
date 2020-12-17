

import Parameters_Entry as pt

class Parameters():
    def __init__(self, CAP, Current, DTE, PE, Alpha, Sharpe, Info, VaR, Credit_Rate, IndLife, MStar_Rate, Vision_Rate, Experts_Rate):

        self.CAP=float(CAP)
        self.Current = float(Current)
        self.DTE = float(DTE)
        self.PE = float(PE)
        self.Alpha = float(Alpha)
        self.Sharpe = float(Sharpe)
        self.Info = float(Info)
        self.VaR = float(VaR)
        self.Credit_Rate = float(Credit_Rate)
        self.IndLife = float(IndLife)
        self.MStar_Rate = int(MStar_Rate)
        self.Vision_Rate = int(Vision_Rate)
        self.Experts_Rate = int(Experts_Rate)
        

    def get_score(self):
        self.get_score = self.CAP/1000000 + 2 * self.Current/100 - 100/self.DTE + 100/self.PE + (1+self.Sharpe) * (1+self.Info) + (self.Alpha/10)**self.Info + self.Sharpe **(1+self.VaR) + self.Credit_Rate ** (1/self.IndLife) + self.MStar_Rate + self.Vision_Rate + self.Experts_Rate
        return self.get_score


# If the user fails to import the list of parameters for the stickers from Parameters_Entry, Try copying input values here.


def main():
    tp,ticker = pt.Parameters_Entry()
    print("Values inputs for parameters: ",tp,)
    obj1 = Parameters(tp[0],tp[1], tp[2], tp[3], tp[4], tp[5], tp[6], tp[7], tp[8],tp[9],tp[10],tp[11], tp[12])
    print("The score for " + ticker + " is " + str(obj1.get_score()))

main()







'''

def score_process():

    if len(lst_tickers) == 1:
        obj1 = Parameters(*lst_ticker1_parameters)
        print("The score for " + lst_tickers[0] "is " obj1.get_score())

    elif len(lst_tickers) == 2:
        obj1 = Parameters(*lst_ticker1_parameters)
        obj2 = Parameters(*lst_ticker2_parameters)

        print("The score for " + lst_tickers[0] "is " obj1.get_score())
        print("The score for " + lst_tickers[1] "is " obj2.get_score())

    elif len(lst_tickers) == 3:
        obj1 = Parameters(*lst_ticker1_parameters)
        obj2 = Parameters(*lst_ticker2_parameters)
        obj3 = Parameters(*lst_ticker3_parameters)

        print("The score for " + lst_tickers[0] "is " obj1.get_score())
        print("The score for " + lst_tickers[1] "is " obj2.get_score())
        print("The score for " + lst_tickers[2] "is " obj3.get_score())



    elif len(lst_tickers) == 4:
        obj1 = Parameters(*lst_ticker1_parameters)
        obj2 = Parameters(*lst_ticker2_parameters)
        obj3 = Parameters(*lst_ticker3_parameters)
        obj4 = Parameters(*lst_ticker4_parameters)

        print("The score for " + lst_tickers[0] "is " obj1.get_score())
        print("The score for " + lst_tickers[1] "is " obj2.get_score())
        print("The score for " + lst_tickers[2] "is " obj3.get_score())
        print("The score for " + lst_tickers[3] "is " obj4.get_score())


    elif len(lst_tickers) == 5:
        obj1 = Parameters(*lst_ticker1_parameters)
        obj2 = Parameters(*lst_ticker2_parameters)
        obj3 = Parameters(*lst_ticker3_parameters)
        obj4 = Parameters(*lst_ticker4_parameters)
        obj5 = Parameters(*lst_ticker5_parameters)

        print("The score for " + lst_tickers[0] "is " obj1.get_score())
        print("The score for " + lst_tickers[1] "is " obj2.get_score())
        print("The score for " + lst_tickers[2] "is " obj3.get_score())
        print("The score for " + lst_tickers[3] "is " obj4.get_score())
        print("The score for " + lst_tickers[4] "is " obj5.get_score())


    
score_process()








'''

'''
class Parameters():
    def __init__(self, PE_Ratio, EBI, ROE, Debt_To_Equity_Ratio, Current_Ratio, Alpha, Beta, Morning_Star_Rating, Corporate_Bond_Rating, Treynor_Ratio, Info_Ratio, Jurisdiction_Sovereign_Rating, Industry_life_cycle, Position_in_Industry, Expert_Rating_MGT, Expert_Rating_Vision_Goodwill_Execution_Capacities)
    


    def score_Accounting(self)
        
    
    
    def score_Financials(self)


    def score_credit_rating(


    def score_Expert_rating(

'''
    #if tiker represents an index, or an index fund, assign 5 to Morning_Star_Rating, assign Aaa/ to Corporate_Bond_Rating,

        
