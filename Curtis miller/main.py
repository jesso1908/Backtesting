from  __future__ import(absolute_import,division,print_function,unicode_literals)
import backtrader as bt 
from strategy import MovingAverage
from analyzer import AcctStats
from positionsize import propsizer
import random
from observer import AcctValue
import datetime as dt
import pandas as pd 
# from analyzers import printTradeAnalysis,printSQN
import json
from foward_analysis import windows
from copy import deepcopy






datapath="E:/sublime/assignment/Data cleaning/Nifty-1D.csv"
# datapath="F:/Zerodha data/BankNifty futures continuous\Bankniftyfutures1.csv"

if __name__=="__main__":
	## Trainer
	# cerebro=bt.cerebro()
	
	trainer = bt.Cerebro(maxcpus=1,stdstats=False)    # Object for optimization (setting maxcpus to 1
									 # cuz parallelization throws errors; why?)
	trainer.broker.set_cash(10000000)
	trainer.broker.setcommission(0.02)

	# cerebro.addstrategy(MovingAverage)
	trainer.optstrategy(MovingAverage,optim=True,optim_fs=windows)
	
	data=bt.feeds.GenericCSVData(
	dataname=datapath,
	fromdate=dt.datetime(2011,1,3),
	todate=dt.datetime(2015,12,3),
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
	
	trainer.adddata(data)
	trainer.addanalyzer(AcctStats)
	trainer.addsizer(propsizer)
	tester = deepcopy(trainer)
	res =trainer.run()
	# Get optimal combination
	opt_res = pd.DataFrame({r[0].params.optim_fs: r[0].analyzers.acctstats.get_analysis() for r in res}
					   ).T.loc[:, "return"].sort_values(ascending=False).index[0]
	print(opt_res)



	tester.addstrategy(MovingAverage, optim=True, optim_fs=opt_res)   # Test with optimal combination
	data_1=bt.feeds.GenericCSVData(
	dataname=datapath,
	fromdate=dt.datetime(2016,4,10),
	todate=dt.datetime(2020,1,1),
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
	tester.adddata(data_1)
 
 
	res = tester.run()
	# res_dict = res[0].analyzers.acctstats.get_analysis() for r in res 
	# res_dict["fast"], res_dict["slow"] = opt_res
	# # res_dict["start_date"] = datafeeds["AAPL"].iloc[test[0]].name
	# # res_dict["end_date"] = datafeeds["AAPL"].iloc[test[-1]].name
	# walk_forward_results.append(res_dict)
	# wfdf = pd.DataFrame(walk_forward_results)
	# print(wfdf)




# cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
# cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")
# cerebro.addanalyzer(bt.analyzers.Calmar,_name="Calmar")
# cerebro.addanalyzer(bt.analyzers.SharpeRatio,_name="Sharpe")
# cerebro.addanalyzer(bt.analyzers.DrawDown,_name="drawdown")
# cerebro.addanalyzer(bt.analyzers.AnnualReturn,_name="annualreturn")
# cerebro.addanalyzer(bt.analyzers.Returns,_name="return")
# cerebro.addanalyzer(bt.analyzers.VWR,_name="vwr")
# cerebro.addanalyzer(bt.analyzers.TimeDrawDown,_name="timedrawdown")

# cerebro.addobserver(bt.observers.Trades)
# cerebro.addobserver(bt.observers.DrawDown)
# cerebro.addobserver(bt.observers.BuySell)
# cerebro.addwriter(bt.WriterFile,csv=True,out="Output/data.csv")





	# print("Starting portfolio value :",cerebro.broker.getvalue())
	# res =cerebro.run(stdstats=False)
	# cerebro.plot(iplot=True,volume=False)
# firstStrat = strategies[0]
# printTradeAnalysis(firstStrat.analyzers.ta.get_analysis())
# printSQN(firstStrat.analyzers.sqn.get_analysis())
	# print("Final portfolio value :",cerebro.broker.getvalue())
# return_opt = pd.DataFrame({r[0].params.optim_fs: r[0].analyzers.acctstats.get_analysis() for r in res}
# 					  ).T.loc[:, ['end', 'growth', 'return']]
# print(return_opt.sort_values("return"))
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
# sqn_analyzer.close()





