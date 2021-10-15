import backtrader as bt
import backtrader.indicators as btind
from datetime import time
from indicators import SwingInd
from indicators import Extrema
import datetime

class percent(bt.Strategy):
	def __init__(self):
		self.dataclose = self.datas[0].close
		self.pct_change = bt.ind.PctChange(self.dataclose,period=12)
		self.pct_change =self.
		# self.avg = bt.ind.Average(self.pct_change,period =100)
		
		
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
		# self.order=None
	 
	def next(self):
		


		# print(self.datas[0].datetime.datetime(0),self.pct_change[0])

	


		
