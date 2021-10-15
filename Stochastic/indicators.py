import backtrader as bt 
class Stochastic(bt.Indicator):

	lines =("value","oscillator",)
	params = (("lookback",14),("d_period",3),)
	
	def __init__(self):
		self.dataclose =self.datas[0].close
		self.datahigh =self.datas[0].high 
		self.datalow = self.datas[0].low

		
		self.lowest = bt.ind.Lowest(self.datalow,period=self.p.lookback)
		self.highest= bt.ind.Highest(self.datahigh,period=self.p.lookback)
		k_value= ((self.dataclose - self.lowest) / (self.highest-self.lowest) ) * 100
		self.lines.oscillator =k_value

		self.lines.value= bt.ind.SMA(k_value,period =self.params.d_period)

