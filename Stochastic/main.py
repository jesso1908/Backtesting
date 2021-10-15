from  __future__ import(absolute_import,division,print_function,unicode_literals)
import backtrader as bt 
from strategy import Firststrategy

import datetime as dt
if __name__=="__main__":
	cerebro=bt.Cerebro()
	cerebro.addstrategy(Firststrategy)
	datapath="E:/sublime/assignment/Data cleaning/Nifty-1D.csv"
	data=bt.feeds.GenericCSVData(

	dataname=datapath,
	fromdate=dt.datetime(2009,1,1),
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
	cerebro.adddata(data)
	cerebro.broker.setcash(1000000.00)
	print("Starting portfolio value :",cerebro.broker.getvalue())
	cerebro.run()
	print("Final portfolio value :",cerebro.broker.getvalue())
