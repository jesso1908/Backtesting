import backtrader as bt
import backtrader.indicators as btind
from datetime import time
from slope import support_resistance
class Strategyone(bt.Strategy):

	def __init__(self):
		self.symbol = support_resistance(self.datas[0])
		



		
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
		print(self.symbol.swings[0])
		print(self.symbol.signal[0])
		

		
		
		


		
			