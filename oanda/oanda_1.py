import backtrader as bt 
import btoandav20 as bto 
import datetime
oanda_access_token = "7d6c67c4620a9954cfcc17836d02c1ba-eaa694ba7cece2125a59eeba08d589ad"
acc = "101-002-18654862-001"

class mystrategy(bt.Strategy):
	def __init__(self):
		self.breaker =1
		print("Intializing strategy")
	def log_data(self):
		ohlcv = []
		ohlcv.append(str(self.data.datetime.datetime()))
		ohlcv.append(str(self.data.open[0]))
		ohlcv.append(str(self.data.high[0]))
		ohlcv.append(str(self.data.low[0]))
		ohlcv.append(str(self.data.close[0]))
		ohlcv.append(str(self.data.volume[0]))
		print(",".join(ohlcv))




	def next(self):
		self.log_data()
	
		

def start():
	print("Starting backtrader")
	cerebro = bt.Cerebro()
	store = bto.stores.OandaV20Store(token=oanda_access_token, account=acc, practice=True,notif_transactions = False,stream_timeout=50)
	datakwargs = dict(timeframe=bt.TimeFrame.Seconds,compression=1,tz='Canada/Eastern',backfill=False,backfill_start=False,)
	data = store.getdata(dataname="EUR_USD", **datakwargs)
	data.resample(timeframe=bt.TimeFrame.Seconds,compression=10)  # rightedge=True, boundoff=1)
	cerebro = bt.Cerebro()
	cerebro.adddata(data)
	cerebro.setbroker(store.getbroker())
	cerebro.addstrategy(mystrategy)
	cerebro.run()
start()