import backtrader as bt
import backtrader.indicators as btind
from datetime import time

class turtle(bt.Strategy):
	def __init__(self):
		self.dataclose=self.datas[0].close
		self.highest =self.datas[0].high(-1) 
		self.lowest = self.datas[0].low(-1)
		self.period_high = btind.Highest(self.highest,period=20)
		self.period_low =btind.Lowest(self.lowest,period=20)
		self.average =btind.Average(self.datas[0].close(-1),period=20)
		
		
		
		
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
		# self.order=None
	 
	def next(self):
		print(self.dataclose[0])
		if not self.position:
			if self.dataclose[0] > self.period_high[0]:
				print("Buy order Created",self.dataclose[0])
				self.order = self.buy()

			elif self.dataclose[0] < self.period_low[0]:
				print("Sell order Created",self.dataclose[0])
				self.order = self.sell()
		else:
			if self.order.isbuy():
				if self.dataclose[0] < self.average[0]:
					print("Buy Closed",self.dataclose[0])
					self.close()
			elif self.order.issell():
				if self.dataclose[0] > self.average[0]:
					print("Sell Closed",self.dataclose[0])
					self.close()
		# print("close:",self.dataclose[0])
		# print("high:",self.highest[0])
		



		
			