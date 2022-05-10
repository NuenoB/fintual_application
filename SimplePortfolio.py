# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:30:25 2022

@author: enzoc
"""


from Stocks import Stock
from datetime import datetime, timedelta

class SimplePortfolio():
    """ A simple portafolio that calculate the profits of its stocks"""


    # stocks = None
    def __init__(self):
        self.stocks = None

    def SetStocks(self, input_stocks):
        """
        set the list of stocks

        Parameters
        ----------
        input_stocks : list of stock
            list of stock.

        Returns
        -------
        None.

        """
        self.stocks = input_stocks


    def __cumulative_return(self, initial_value: float, final_value:float):
        # This function shuld be in stock
        cumulative_return = ((final_value - initial_value )
                         / (initial_value) )

        return cumulative_return

    def __annualized_return(self, initial_date: datetime, final_date:datetime,
                            initial_value: float, final_value:float):

        ddate = initial_date - final_date
        n_days = ddate.days

        cumulative_return = self.__cumulative_return(initial_value, final_value)

        annualized_return = pow((1 + cumulative_return),365/n_days)-1

        return annualized_return


    def Profit(self, initial_date:datetime, final_date:datetime):
        """
        calculate portfolio profit


        Parameters
        ----------
        initial_date : datetime
            DESCRIPTION.
        final_date : datetime
            DESCRIPTION.

        Returns
        -------
        total_profit : double
            DESCRIPTION.

        """


        total_profit = 0
        for stock in self.stocks:
            # get profits
            initial_value = stock.Profit(initial_date)
            final_value = stock.Profit(final_date)


            #get annualized return
            annual_return = self.__annualized_return(initial_date, final_date,
                                                     initial_value,final_value)

            total_profit = total_profit + annual_return


        return total_profit

