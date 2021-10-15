import backtrader as bt
import backtrader.indicators as btind
from datetime import time
from indicators import SwingInd
class MovingAverage(bt.Strategy):
	def __init__(self):

		self.crossover=[]
		# self.inds=dict()
		for d in self.datas:
			self.sma_5=btind.SMA(d,period=5)
			self.sma_10=btind.SMA(d,period=10)
			self.crossover.append(btind.CrossOver(self.sma_5,self.sma_10))
			self.rsi=btind.RSI(d,period=9)
			# self.stocha=btind.StochasticSlow(d,safediv=True,period=14,period_dfast=3,period_dslow=3)
			self.candletracker=0
			self.order=None


			# self.inds[d] = dict()
			# self.inds[d]["sma_5"] = btind.SMA(d.close,period=10)
			# self.inds[d]["sma_10"]=btind.SMA(d.close,period=50)
			# self.inds[d]["crossover"]=btind.CrossOver(self.inds[d]["sma_5"],self.inds[d]["sma_10"])
			# self.inds[d]["rsi"]=btind.RSI(d,period=9)
			# self.inds[d]["stocha"] = btind.StochasticSlow(d, safediv = True, period=14, period_dfast=3, period_dslow=3)
			# self.inds[d]["candletracker"]=0
			# self.inds[d]["order"]=None
		
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
		
		for i,d in enumerate(self.datas):
			if not self.getposition(d).size:
				if self.crossover[i] > 0 and self.rsi[i] > 50:
					self.order=self.buy(data=d)
				elif self.crossover[i] < 0 and self.rsi < 50:
					self.order=self.sell(data=d)
			else:
				self.candletracker += 1
				if self.candletracker > 10:
					self.close(data=d)
			

			
			# print(self.inds[d]["crossover"])
			# if not self.getpositions(d).size:
			# 	if self.inds[d]["crossover"] == 1 and self.inds[d]["rsi"] >50:
			# 		self.inds[d]["order"]=self.buy(data=d)
			# 		print("buy order executed")
			# 	elif self.crossover == -1 and self.rsi <50:
			# 		self.inds[d]["order"]=self.sell(data=d)
			# 		print("sell order executed")
			# else:
			# 	self.inds[d]["candletracker"] += 1
			# 	if self.inds[d]["candletracker"] > 10:
			# 		self.close(data=d)
			# 		print("position closed")
	def stop(self):
		self.log(f"Ending value {self.broker.getvalue()}")



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

		
			