
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