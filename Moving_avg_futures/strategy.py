import backtrader as bt
import backtrader.indicators as btind
from datetime import time
from indicators import SwingInd
from indicators import Extrema
class MovingAverage(bt.Strategy):
	def __init__(self):
		self.sma_5 = btind.SMA(period=5)
		self.sma_10=btind.SMA(period=10)
		self.crossover=btind.CrossOver(self.sma_5,self.sma_10)
		self.rsi=btind.RSI(self.datas[0],period=9)
		self.stocha = btind.StochasticSlow(self.datas[0], safediv = True, period=14, period_dfast=3, period_dslow=3)
		self.candletracker=0
		
	def log(self,txt):
		print(txt)
	def notify_order(self,order):
		if order.status in [order.Submitted,order.Accepted]:
			return
		if order.status in [order.Completed]:
			if order.isbuy():
				self.log(str(self.datas[0].datetime.date(0))+" Buy executed "+str(order.executed.price)+"\tcomm"+str(order.executed.comm)+"\t size"+str(order.executed.size))
				self.buyprice = order.executed.price
			else:

				self.log(str(self.datas[0].datetime.date(0))+" Sell executed "+str(order.executed.price)+"\t comm"+str(order.executed.comm)+"\t size"+str(order.executed.size))

		elif order.status in [order.Canceled,order.Margin,order.Rejected]:
			self.log("Order cancelled/margin snot sufficient/rejected")
		self.order=None
	 
	def next(self):
		# print(self.broker.get_leverage())
		if not self.position:
			if self.crossover == 1 and self.rsi >50:
				self.order=self.buy()
			elif self.crossover == -1 and self.rsi <50:
				self.order=self.sell()
		else:
			self.candletracker += 1
			if self.candletracker > 10:
				self.close()

class Swingstrategy(bt.Strategy):
	def __init__(self):
		self.swing = SwingInd(self.datas[0])
		self.candletracker=0 
		self.order=None
	def next(self):
		print(self.swing[0])
		# if not self.position:
		# 	if self.swing[0]==1:
		# 		self.order=self.buy()
		# 	elif self.swing[0]==-1:
		# 		self.order==self.sell()
		# else:
		# 	self.candletracker +=1
		# 	if self.candletracker > 5:
		# 		self.close()
		# 		self.candletracker=0

		
class chart_detection(bt.Strategy):
	def __init__(self):
		self.extrem = Extrema(self.datas[0])
	def next(self):
		print(self.extrem[0])