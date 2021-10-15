import backtrader as bt 

class support_resistance(bt.Indicator):
    def __init__(self):
        params = (("periods",20),)

        self.resistance_level = bt.ind.Highest(self.data,period = self.p.periods,plot=True)
        self.support_level = bt.ind.lowest(self.data,period=self.p.periods,plot=True)
        self.range_level = self.resistance_level - self.support_level
        self.resistance_tolerance = self.resistance_level + ( 0.2 * range_level )
        self.support_level = self.support_level + (0.2 * range_level)
        
        # self.minimum_period = (self.p.periods * 4) + 1
        # self.addminperiod(self.minimum_period)


#    
# class support_resistance(bt.Indicator):
    '''
    A Simple swing indicator that measures swings (the lowest/highest value)
    within a given time period.
    '''
    # lines = ('swings', 'signal')
    # params = (('period',14),)
 
    # def __init__(self):
 
        #Set the swing range - The number of bars before and after the swing
        #needed to identify a swing
    #     self.swing_range = (self.p.period * 2) +1 
    #     self.addminperiod(self.swing_range)
 
    # def next(self):
    #     #Get the highs/lows for the period
    #     highs = self.datas[0].high.get(size=self.swing_range)
    #     lows = self.datas[0].low.get(size=self.swing_range)
    #     #check the bar in the middle of the range and check if greater than rest
    #     if highs.pop(self.p.period) > max(highs):
    #         # self.lines.swings[-self.p.period] = 1 #add new swing
    #         self.lines.signal[0] = 1 #give a signal
    #     elif lows.pop(self.p.period) < min(lows):
    #         # self.lines.swings[-self.p.period] = -1 #add new swing
    #         self.lines.signal[0] = -1 #give a signal
    #     else:
    #         self.lines.swings[-self.p.period] = 0
    #         self.lines.signal[0] = 0





