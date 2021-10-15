import backtrader as bt
class CommNifty(bt.CommInfoBase):
	params = (("stocklike",False),("commtype",bt.CommInfoBase.COMM_PERC),("stampduty",0.00002))
	def _getcommission(self,size,price,pseudoexec):
		if size > 0:
			return  (abs(size) * price * self.p.commission * self.p.mult) + (abs(size) * price * self.p.stampduty * self.p.mult)
		elif size < 0:
			return  abs(size) * price * self.p.commission * self.p.mult
		else:
			return 0

