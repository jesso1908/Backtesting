import backtrader as bt 
import math
class propsizer(bt.Sizer):
    params = (('prop',0.1),("batch",100),)
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            target = self.broker.getvalue() * self.params.prop 
            price = data.close[0]
            shares_ideal = target/price
            batches = int(shares_ideal/self.params.batch)
            shares = batches * self.params.batch 
            if shares * price > cash :
                return 0
            else:
                return shares 
        else:
            return self.broker.getposition(data).size 
    	## called everytime when self.buy or self.sell is made in strategy subclass,without stating the size of order

        # return self.p.size
# class maxRiskSizer(bt.Sizer):
#     '''
#     Returns the number of shares rounded down that can be purchased for the
#     max rish tolerance
#     '''
#     params = (('risk', 0.3),)

#     def __init__(self):
#         if self.p.risk > 1 or self.p.risk < 0:
#             raise ValueError('The risk parameter is a percentage which must be'
#                 'entered as a float. e.g. 0.5')

#     def _getsizing(self, comminfo, cash, data, isbuy):
#         if isbuy == True:
#             size = math.floor((cash * self.p.risk) / data[0])
#         else:
#             size = math.floor((cash * self.p.risk) / data[0]) * -1
#         return size