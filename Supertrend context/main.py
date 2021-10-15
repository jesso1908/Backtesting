from  __future__ import(absolute_import,division,print_function,unicode_literals)
import backtrader as bt 
from analyzers import printTradeAnalysis,printSQN
from strategy import Superstrat



import datetime as dt
# from analyzers import printTradeAnalysis,printSQN
import json
from glob import glob

datapath1 = "E:/Backtest project/Supertrend context/Data/BANKNIFTY_F1_5min.csv"
datapath2 = "E:/Backtest project/Supertrend context/Data/BANKNIFTY_F1_60min.csv"
if __name__=="__main__":
	cerebro=bt.Cerebro()
	cerebro.addstrategy(Superstrat)
	data=bt.feeds.GenericCSVData(
	dataname=datapath1,
	fromdate=dt.datetime(2009,7,17),
	todate=dt.datetime(2010,12,30),
	datetime=0,
	timeframe=bt.TimeFrame.Minutes,
	compression=1,
	dtformat=("%Y-%m-%d %H:%M:%S"),
	open=1,
	high=2,
	low=3,
	close=4,
	openinterest=-1,
	volume=-1,
	reverse=False,
	header=0
	)
	data2=bt.feeds.GenericCSVData(
	dataname=datapath2,
	fromdate=dt.datetime(2009,7,17),
	todate=dt.datetime(2010,12,30),
	datetime=0,
	timeframe=bt.TimeFrame.Minutes,
	compression=1,
	dtformat=("%Y-%m-%d %H:%M:%S"),
	open=1,
	high=2,
	low=3,
	close=4,
	openinterest=-1,
	volume=-1,
	reverse=False,
	header=0
	)

	cerebro.broker.setcash(1000000.00)
	cerebro.adddata(data)
	cerebro.adddata(data2)



	cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
	cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")
	cerebro.addanalyzer(bt.analyzers.Calmar,_name="Calmar")
	cerebro.addanalyzer(bt.analyzers.SharpeRatio,_name="Sharpe")
	cerebro.addanalyzer(bt.analyzers.DrawDown,_name="drawdown")
	cerebro.addanalyzer(bt.analyzers.AnnualReturn,_name="annualreturn")
	cerebro.addanalyzer(bt.analyzers.Returns,_name="return")
	cerebro.addanalyzer(bt.analyzers.VWR,_name="vwr")
	cerebro.addanalyzer(bt.analyzers.TimeDrawDown,_name="timedrawdown")

# cerebro.addobserver(bt.observers.Trades)
# cerebro.addobserver(bt.observers.DrawDown)
# cerebro.addobserver(bt.observers.BuySell)
# cerebro.addwriter(bt.WriterFile,csv=True,out="Output/data.csv")





	print("Starting portfolio value :",cerebro.broker.getvalue())
	# cerebro.run()
	# print("Ending portfolio value: ",cerebro.broker.getvalue())
strategies=cerebro.run()
firstStrat = strategies[0]
printTradeAnalysis(firstStrat.analyzers.ta.get_analysis())
printSQN(firstStrat.analyzers.sqn.get_analysis())
print("Ending portfolio value: ",cerebro.broker.getvalue())
	# print("Final portfolio value :",cerebro.broker.getvalue())
	# cerebro.plot(style='candlestick')

	# annualreturnanalyzer = open(r"Output/annualreturnanalayzer.txt","w+")
	# drawdownanalyzer = open(r"Output/drawndownanalayzer.txt","w+")
	# sharperatioanalyzer = open(r"Output/sharperatioanalayzer.txt","w+")
	# vwranalyzer  = open(r"Output/vwranalayzer.txt","w+")
	# returnanalyzer = open(r"Output/returnanalayzer.txt","w+")
	# tradeanalyzer  = open(r"Output/tradeanalayzer.txt","w+")
	# time_drawdown_analyzer=open(r"Output/timedrawdownanalayzer.txt","w+")
	# sqn_analyzer=open(r"Output/sqnanalayzer.txt","w+")

	# annualreturnanalyzer.write(json.dumps(firstStrat.analyzers.getbyname("annualreturn").get_analysis()))
	# drawdownanalyzer.write(json.dumps(firstStrat.analyzers.getbyname("drawdown").get_analysis()))
	# sharperatioanalyzer.write(json.dumps(firstStrat.analyzers.getbyname("Sharpe").get_analysis()))
	# vwranalyzer.write(json.dumps(firstStrat.analyzers.getbyname("vwr").get_analysis()))
	# returnanalyzer.write(json.dumps(firstStrat.analyzers.getbyname("return").get_analysis()))
	# tradeanalyzer.write(str(firstStrat.analyzers.getbyname("ta").get_analysis()))
	# time_drawdown_analyzer.write(json.dumps(firstStrat.analyzers.getbyname("timedrawdown").get_analysis()))
	# sqn_analyzer.write(json.dumps(firstStrat.analyzers.getbyname("sqn").get_analysis()))

	# annualreturnanalyzer.close()
	# drawdownanalyzer.close()
	# sharperatioanalyzer.close()
	# vwranalyzer.close()
	# returnanalyzer.close()
	# tradeanalyzer.close() 
	# time_drawdown_analyzer.close()
	#sqn_analyzer.close()





