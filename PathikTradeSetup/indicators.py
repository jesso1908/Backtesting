import backtrader as bt 
class Stochastic(bt.Indicator):
	pass

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

class SwingInd(bt.Indicator):
    '''
    A Simple swing indicator that measures swings (the lowest/highest value)
    within a given time period.
    '''
    lines = ('swings', 'signal')
    params = (('period',7),)
 
    def __init__(self):
 
        #Set the swing range - The number of bars before and after the swing
        #needed to identify a swing
        self.swing_range = (self.p.period * 2) + 1
        self.addminperiod(self.swing_range)
 
    def next(self):
        #Get the highs/lows for the period
        highs = self.data.high.get(size=self.swing_range)
        lows = self.data.low.get(size=self.swing_range)
        #check the bar in the middle of the range and check if greater than rest
        if highs.pop(self.p.period) > max(highs):
            self.lines.swings[-self.p.period] = 1 #add new swing
            self.lines.signal[0] = 1 #give a signal
        elif lows.pop(self.p.period) < min(lows):
            self.lines.swings[-self.p.period] = -1 #add new swing
            self.lines.signal[0] = -1 #give a signal
        else:
            self.lines.swings[-self.p.period] = 0
            self.lines.signal[0] = 0