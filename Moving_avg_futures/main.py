from  __future__ import(absolute_import,division,print_function,unicode_literals)
import backtrader as bt 
from strategy import MovingAverage
from strategy import chart_detection
from positionsize import examplesizer
from positionsize import maxRiskSizer
import datetime as dt
from commision import CommNifty
# from analyzers import printTradeAnalysis,printSQN
import json
# 


datapath="E:/Backtesting pandas/Data/Nifty-1D.csv"
# datapath="F:/Zerodha data/BankNifty futures continuous\Bankniftyfutures1.csv"

if __name__=="__main__":
	cerebro=bt.Cerebro()
	commission = CommNifty(commission=0.03,mult=75,margin=100000)
	cerebro.addstrategy(chart_detection)
	data=bt.feeds.GenericCSVData(
	dataname=datapath,
	fromdate=dt.datetime(2008,1,1),
	todate=dt.datetime(2018,1,1),
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
cerebro.addsizer(bt.sizers.FixedSize,stake=1)
# cerebro.addsizer(maxRiskSizer,risk=0.05)
cerebro.broker.setcash(500000.00)
# cerebro.broker.setcommission(commission=20.0, margin=100000.0, mult=50.0)
cerebro.broker.addcommissioninfo(commission)



cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")
cerebro.addanalyzer(bt.analyzers.Calmar,_name="Calmar")
cerebro.addanalyzer(bt.analyzers.SharpeRatio,_name="Sharpe")
cerebro.addanalyzer(bt.analyzers.DrawDown,_name="drawdown")
cerebro.addanalyzer(bt.analyzers.AnnualReturn,_name="annualreturn")
cerebro.addanalyzer(bt.analyzers.Returns,_name="return")
cerebro.addanalyzer(bt.analyzers.VWR,_name="vwr")
cerebro.addanalyzer(bt.analyzers.TimeDrawDown,_name="timedrawdown")
cerebro.addanalyzer(bt.analyzers.PyFolio,_name="portfolio")

cerebro.addobserver(bt.observers.Trades)
cerebro.addobserver(bt.observers.DrawDown)
cerebro.addobserver(bt.observers.BuySell)
# cerebro.addwriter(bt.WriterFile,csv=True,out="Output/data.csv")





print("Starting portfolio value :",cerebro.broker.getvalue())
strategies = cerebro.run()
# cerebro.plot()

# positions, transactions, gross_lev = strategies[0].analyzers.pyfolio.get_pf_items()
# pf.create_round_trip_tear_sheet(returns, positions, transactions)
# firstStrat = strategies[0]
# printTradeAnalysis(firstStrat.analyzers.ta.get_analysis())
# printSQN(firstStrat.analyzers.sqn.get_analysis())
print("Final portfolio value :",cerebro.broker.getvalue())
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





