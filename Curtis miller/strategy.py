import backtrader as bt
import backtrader.indicators as btind
from datetime import time

class MovingAverage(bt.Strategy):
	params = (("fast",5),("slow",10),("optim",False),("optim_fs",(5,10)),)
	def __init__(self):
		if self.params.optim:
			self.params.fast,self.params.slow = self.params.optim_fs
		if self.params.fast > self.params.slow:
			raise ValueError("Fast should be smaller than slow moving average")
		self.fast_ma = dict()
		self.slow_ma = dict()
		self.regime = dict()
		for d in self.getdatanames():
			self.fast_ma[d] = btind.SMA(self.getdatabyname(d),period=self.params.fast,plotname="FAST SMA:"+d)
			self.slow_ma[d] = btind.SMA(self.getdatabyname(d),period=self.params.slow,plotname="SLOW SMA:" +d)
			self.regime[d] = self.fast_ma[d] - self.slow_ma[d]


		
	# def log(self,txt):
	# 	print(txt)
	# def notify_order(self,order):
	# 	if order.status in [order.Submitted,order.Accepted]:
	# 		return
	# 	if order.status in [order.Completed]:
	# 		if order.isbuy():
	# 			self.log(str(self.datas[0].datetime.date(0))+" Buy executed "+str(order.executed.price))
	# 		else:

	# 			self.log(str(self.datas[0].datetime.date(0))+" Sell executed "+str(order.executed.price))
	# 	elif order.status in [order.Canceled,order.Margin,order.Rejected]:
	# 		self.log("Order cancelled/margin snot sufficient/rejected")
	# 	self.order=None
	 
	def next(self):
		for d  in self.getdatanames():
			pos = self.getpositionbyname(d).size
			if pos == 0:
				if self.regime[d][0] > 0 and  self.regime[d][-1] <= 0:
					self.buy(data=self.getdatabyname(d))
			else :
				if self.regime[d][0] <=  0 and self.regime[d][-1] > 0:
					self.sell(data=self.getdatabyname(d))

		
			