import backtrader as bt
import backtrader.indicators as btind
from datetime import time
from indicators import SuperTrend
from indicators import SuperTrendBand
class Superstrat(bt.Strategy):
	def __init__(self):
		self.dataclose =self.datas[0].close
		self.dataclose1 = self.datas[1].close
		self.supertrend_5m = SuperTrend(self.datas[0])
		self.supertrend_15m = SuperTrend(self.datas[1],period=10,multiplier=3)
		self.candletracker=0



		
	def log(self,txt):
		print(txt)
	def notify_order(self,order):
		if order.status in [order.Submitted,order.Accepted]:
			return
		if order.status in [order.Completed]:
			if order.isbuy():
				self.log(str(self.datas[0].datetime.date(0))+" Buy executed "+str(order.executed.price))
			else:

				self.log(str(self.datas[0].datetime.date(0))+" Sell executed "+str(order.executed.price))
		elif order.status in [order.Canceled,order.Margin,order.Rejected]:
			self.log("Order cancelled/margin snot sufficient/rejected")
		self.order=None
	 
	def next(self):
		# print(self.datas[0].datetime.datetime(0),self.dataclose[0])
		# print(self.datas[1].datetime.datetime(0),self.dataclose1[0])
		# print(self.datas[0].datetime.datetime(0),self.supertrend_5m[0])
		# print(self.datas[1].datetime.datetime(0),self.supertrend_15m[0])
		if not self.position:
			if self.dataclose1[0] > self.supertrend_15m[0]:
				if self.dataclose[0] > self.supertrend_5m[0]:
					self.order=self.buy()
		else:
			self.candletracker += 1
			if self.candletracker > 5:
				self.close()
				self.candletracker=0
				# self.stoporder=self.sell(exectype=bt.Order.Stop,price=self.dataclose*0.095)

		
		
		


		
			