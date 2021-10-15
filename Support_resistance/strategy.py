import backtrader as bt
import backtrader.indicators as btind
from datetime import time
from slope import support_resistance
class Strategyone(bt.Strategy):
	params = (("periods",20),)

	def __init__(self):
		self.dataclose = self.datas[0].close
		self.resistance_level = bt.ind.Highest(self.data,period = self.p.periods)
		self.support_level = bt.ind.Lowest(self.data,period = self.p.periods)
		range_level = self.resistance_level - self.support_level
		self.resistance_tolerance = self.resistance_level - ( 0.2 * range_level )
		self.support_tolerance = self.support_level + (0.2 * range_level)
		self.in_support=0
		self.in_resistance=0
		# self.minimum_period = (self.p.periods * 4) + 1
		# self.addminperiod(self.minimum_period)
		
		
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
		
	 
	def next(self):
		print(self.datetime.date(),self.dataclose[0])
		if not self.position:
			if self.dataclose[0] > self.resistance_tolerance[0] and self.dataclose[0] < self.resistance_level[0]:
				self.order=self.buy()
		elif self.dataclose[0] < self.support_tolerance[0] and self.dataclose[0] < self.support_level[0]:
				self.order = self.sell()
		# print(self.datetime.date())
		# print("support level",self.support_level[0])
		# print("\t support_tolerance",self.support_tolerance[0])

		# print("resitance level",self.resistance_level[0])
		# print("\t resistance_tolerance",self.resistance_tolerance[0])
		
		# if self.dataclose[0] > self.resistance_tolerance[0] and self.dataclose[0] < self.resistance_level[0]:
		# 	self.in_support += 1
		# elif self.dataclose[0] < self.support_tolerance[0] and self.dataclose[0] > self.support_level[0]:
		# 	self.in_resistance += 1
		# if not self.position:
		# 	if self.in_support > 2:
		# 		self.order=self.buy()
		# 		self.in_support=0
		# 		print("sell order created",self.dataclose[0])
		# 	elif self.in_resistance > 2:
		# 		self.order=self.sell()
		# 		self.in_resistance=0
		# 		print("Buy Order created",self.dataclose[0])
			
		
		

		
		
		


		
			