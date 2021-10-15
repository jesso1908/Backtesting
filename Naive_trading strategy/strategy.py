import backtrader as bt
import backtrader.indicators as btind
from datetime import time

class native(bt.Strategy):
	def __init__(self):
		self.dataclose= self.datas[0].close
		self.consc_day=0
		
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
			if self.dataclose[0] > self.dataclose[-1]:
				self.consc_day +=1
				if self.consc_day > 5:
					self.order = self.buy()
					self.consc_day=0
			elif self.dataclose[0] < self.dataclose[-1]:
				self.consc_day -= 1
				if self.consc_day < -5:
					self.order = self.sell()
					self.consc_day=0
		else:
			if self.order.isbuy():
				if self.dataclose[0] < self.dataclose[-1]:
					self.consc_day -= 1
					if self.consc_day < -5:
						self.close()
						self.consc_day=0
			elif self.order.issell():
				if self.dataclose[0] > self.dataclose[-1]:
					self.consc_day += 1
					if self.consc_day > 5:
						self.close()
						self.consc_day = 0
		



		
			