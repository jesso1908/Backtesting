import backtrader as bt 
from scipy.signal import argrelextrema
import numpy as np 
import pandas as pd 
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
class Extrema(bt.Indicator):
    '''
    Find local price extrema. Also known as highs and lows.

        Formula:
        - https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.argrelextrema.html

        See also:
        - https://analyzingalpha.com/algorithmic-pattern-detection

        Aliases: None
        Inputs: high, low
        Outputs: he, le
        Params:
        - period N/A
    '''
    lines = 'lmax',  'lmin'

    def next(self):

        # Get all days using ago with length of self
        past_highs = np.array(self.data.high.get(ago=0, size=len(self)))
        past_lows = np.array(self.data.low.get(ago=0, size=len(self)))

        # Use argrelextrema to find local maxima and minima
        last_high_days = argrelextrema(past_highs, np.greater)[0] \
            if past_highs.size > 0 else None
        last_low_days = argrelextrema(past_lows, np.less)[0] \
            if past_lows.size > 0 else None

        # Get the day of the most recent local maxima and minima
        last_high_day = last_high_days[-1] \
            if last_high_days.size > 0 else None
        last_low_day = last_low_days[-1] \
            if last_low_days.size > 0 else None

        # Use local maxima and minima to get prices
        last_high_price = past_highs[last_high_day] \
            if last_high_day else None
        last_low_price = past_lows[last_low_day] \
            if last_low_day else None

        # If local maxima have been found, assign them
        if last_high_price:
            self.l.lmax[0] = last_high_price

        if last_low_price:
            self.l.lmin[0] = last_low_price