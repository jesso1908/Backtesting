import backtrader as bt
from datetime import time
class breakout(bt.Strategy):
	def __init__(self):
		self.start_time=time(9,45,00)
		self.end_time=time(12,00,00)
		self.stoptime=time(15,15,00)
		self.pos=0
		self.stoploss_tracker=0
	def log(self,txt):
		print(txt)
	def notify_order(self,order):
		if order.status in [order.Submitted,order.Accepted]:
			return
		if order.status in [order.Completed]:
			if order.isbuy():
				self.log(str(self.datas[0].datetime.datetime(0))+" Buy executed "+str(order.executed.price))
			else:

				self.log(str(self.datas[0].datetime.datetime(0))+" Sell executed "+str(order.executed.price))
		# elif order.status in [order.Canceled,order.Margin,order.Rejected]:
		# 	self.log("Order cancelled/margin snot sufficient/rejected")
		self.order=None
     	# 999647.5499999995
	def next(self):
		# print(self.datas[0].datetime.datetime(0),self.datas[0].close[0])
		# print(self.datas[1].datetime.date(0),self.datas[1].high[0])
		if not self.position and self.stoploss_tracker==0:
			if self.datas[0].datetime.time(0) > self.start_time and self.datas[0].datetime.time(0) < self.end_time:
				if self.datas[0].close[0] > self.datas[1].high[0]:
					self.order=self.buy(data=self.datas[0],exectype=bt.Order.Market)
					self.stoporder=self.sell(data=self.datas[0],exectype=bt.Order.Stop,price=self.datas[0].close-15)
					self.stoploss_tracker=1
					# print("Buy executed ",self.datas[0].datetime.datetime(0),self.datas[0].close[0])
		else:
			if self.datas[0].datetime.time(0) == self.stoptime:
				# print("POSITION EXIT")
				self.cancel(self.stoporder)
				self.close()
				self.stoploss_tracker=0
