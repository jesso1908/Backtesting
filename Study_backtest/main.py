from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pandas as pd 
import numpy as np

import datetime  # For datetime objects
  # To manage paths
# To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt
import datetime as dt 
import pprint


# class AcctStats(bt.Analyzer):
#     """A simple analyzer that gets the gain in the value of the account; should be self-explanatory"""
 
#     def __init__(self):
#         self.start_val = self.strategy.broker.get_value()
#         self.end_val = None
 
#     def stop(self):
#         self.end_val = self.strategy.broker.get_value()
 
#     def get_analysis(self):
#         return {"start": self.start_val, "end": self.end_val,
#                 "growth": self.end_val - self.start_val, "return": self.end_val / self.start_val}


# def printTradeAnalysis(analyzer):
#     '''
#     Function to print the Technical Analysis results in a nice format.
#     '''
#     #Get the results we are interested in
#     total_open = analyzer.total.open
#     total_closed = analyzer.total.closed
#     total_won = analyzer.won.total
#     total_lost = analyzer.lost.total
#     win_streak = analyzer.streak.won.longest
#     lose_streak = analyzer.streak.lost.longest
#     pnl_net = round(analyzer.pnl.net.total,2)
#     strike_rate = (total_won / total_closed) * 100
#     #Designate the rows
#     h1 = ['Total Open', 'Total Closed', 'Total Won', 'Total Lost']
#     h2 = ['Strike Rate','Win Streak', 'Losing Streak', 'PnL Net']
#     r1 = [total_open, total_closed,total_won,total_lost]
#     r2 = [strike_rate, win_streak, lose_streak, pnl_net]
#     #Check which set of headers is the longest.
#     if len(h1) > len(h2):
#         header_length = len(h1)
#     else:
#         header_length = len(h2)
#     #Print the rows
#     print_list = [h1,r1,h2,r2]
#     row_format ="{:<15}" * (header_length + 1)
#     print("Trade Analysis Results:")
#     for row in print_list:
#         print(row_format.format('',*row))

# Create a Stratey
class TestStrategy(bt.Strategy):
    params =(("exitbars",5),)

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.dataclose_previous = self.dataclose(-1)
        self.change = self.dataclose - self.dataclose_previous
        self.signal_1 = bt.If(self.change > 0, 1,0)

        # Keep a reference to the "close" line in the data[0] dataseries
        
        self.order = None

    def notify_trade(self, trade):
        self.mytrade = trade
        # if not trade.isclosed:
        #     return

        # self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
        #          (trade.pnl, trade.pnlcomm))


        # Something like this when operating on a single data source
        # if self.position:  # in the market
        #     # for sure there is an open trade  - get the info that was added to the opening order
        #     info = self.trade.history[0].event.order.info
        #     self.log(info)
    # def notify_order(self, order):
    #     if order.status in [order.Submitted, order.Accepted]:
    #         # Buy/Sell order submitted/accepted to/by broker - Nothing to do
    #         return

    #     # Check if an order has been completed
    #     # Attention: broker could reject order if not enough cash
    #     if order.status in [order.Completed]:
    #         if order.isbuy():
    #             self.log('BUY EXECUTED, %.2f' % order.executed.price)
    #         elif order.issell():
    #             self.log('SELL EXECUTED, %.2f' % order.executed.price)

    #         self.bar_executed = len(self)

    #     elif order.status in [order.Canceled, order.Margin, order.Rejected]:
    #         self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        # self.order = None
    # def prenext(self):
    #     print(self.datetime.date(),self.signal_1[0])


    def next(self):
        # available = list(filter(lambda d: len(d), self.datas))
        # print(available[0])
        rets = np.zeros(len(self.datas))
        print(rets)
        for i, d in enumerate(self.datas):
            # calculate individual daily returns
            rets[i] = (d.close[0]- d.close[-1]) / d.close[-1]
            print(rets[i])

        # if self.signal_1[0] > 0 and self.signal_1[-1] < 0
         # print(self.datetime.date(),self.signal_1[0])
        # Simply log the closing price of the series from the reference
        # self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        # if self.order:
        #     return

        # Check if we are in the market
        # if not self.position:

            # Not yet ... we MIGHT BUY if ...
            # if self.dataclose[0] < self.dataclose[-1]:
                    # current close less than previous close

                    # if self.dataclose[-1] < self.dataclose[-2]:
                        # previous close less than the previous close

                        # BUY, BUY, BUY!!! (with default parameters)
                        # self.log('BUY CREATE, %.2f' % self.dataclose[0])

                        # Keep track of the created order to avoid a 2nd order
                        # self.order = self.buy()
                        # self.candletracker = 0

        # else:
            # self.candletracker += 1

            # Already in the market ... we might sell
            # if self.candletracker > self.params.exitbars:
                # SELL, SELL, SELL!!! (with all possible default parameters)
                # self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                # self.order = self.sell()
                # self.candletracker =0

    # def stop(self):
    #  print("exitbars",self.params.exitbars)
    #  print("final value",self.broker.getvalue())





if __name__ == '__main__':




    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy)
    # cerebro.optstrategy(TestStrategy,exitbars = range(5,15))
    datapath = "E:/Backtest project/Study_backtest/Nifty-1D.csv"

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    

    # Create a Data Feed
    data=bt.feeds.GenericCSVData(
    dataname=datapath,
    fromdate=dt.datetime(2008,1,1),
    todate=dt.datetime(2020,6,30),
    datetime=0,
    timeframe=bt.TimeFrame.Days,
    compression=1,
    dtformat=("%Y-%m-%d"),
    open=1,
    high=2,
    low=3,
    close=4,
    openinterest=-1,
    volume=-1,
    reverse=False,
    header=0
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
    # cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")
    # cerebro.addanalyzer(bt.analyzers.Calmar,_name="Calmar")
    # cerebro.addanalyzer(bt.analyzers.SharpeRatio,_name="Sharpe")
    # cerebro.addanalyzer(bt.analyzers.DrawDown,_name="mydrawdown")
    # cerebro.addanalyzer(bt.analyzers.AnnualReturn,_name="annualreturn")
    # cerebro.addanalyzer(bt.analyzers.Returns,_name="return")
    # cerebro.addanalyzer(bt.analyzers.VWR,_name="vwr")
    # cerebro.addanalyzer(bt.analyzers.TimeDrawDown,_name="timedrawdown")
    # cerebro.addanalyzer(bt.analyzers.PyFolio,_name="portfolio")
    # cerebro.addanalyzer(AcctStats,_name="account_statistics")






    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    strat = cerebro.run(tradehistory=True)
    # Annualreturn = pd.DataFrame({i[0].params.exitbars:i[0].analyzers.annualreturn.get_analysis() for i in strat})
    # print(Annualreturn.transpose())
    






    # sharpe =pd.DataFrame({i[0].params.exitbars:i[0].analyzers.Sharpe.get_analysis() for i in strat})
    # print(sharpe.transpose())
    # # pyfolio=strat[0].analyzers.portfolio.get_analysis()
    # # # print(pd.DataFrame(pyfolio).to_csv("portfolio.csv"))
    # # drawdown = pd.DataFrame({i[0].params.exitbars:i[0].analyzers.drawdown.get_analysis() for i in strat})
    # return_opt =pd.DataFrame({r[0].params.exitbars:r[0].analyzers.account_statistics.get_analysis() for r in strat}).T.loc[:, ['end', 'growth', 'return']]
    # # print(return_opt)

    # # return_opt = pd.DataFrame({r[0].params.exitbars: strat[0].analyzers.account_statistics.get_analysis() for r in strat}
    # #                   ).T.loc[:, ['end', 'growth', 'return']]
    # print(return_opt.sort_values("growth",ascending=False))