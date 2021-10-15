import backtrader as bt
from indicators import Stochastic
class Firststrategy(bt.Strategy):
	def __init__(self):
		self.custom = Stochastic(self.datas[0])
	def next(self):
		print(self.datas[0].datetime.date(),self.custom.oscillator[0])