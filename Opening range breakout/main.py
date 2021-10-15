from  __future__ import(absolute_import,division,print_function,unicode_literals)
import backtrader as bt 
from strategy import breakout
import datetime as dt
import pyfolio as pf 
import pandas as pd 
import warnings 
import seaborn as sns
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

def PrintTimeReturn(tmereturn):
	lst_indx = []
	# empty list for monthly retuns
	lst_mnth_ret = []

	#iterate through returns
	for key, value in tmereturn.items():
		lst_indx.append(key)
		lst_mnth_ret.append(value)
	df_ret_mnth = pd.DataFrame(lst_mnth_ret, index=lst_indx)
		
	df_ret_mnth.columns = ['Returns']
	#multiply returns by 100 
	df_ret_mnth['Returns'] = df_ret_mnth['Returns'] *100
	#Add year month info
	df_ret_mnth['Year'] = df_ret_mnth.index.strftime('%Y')
	df_ret_mnth['Month'] = df_ret_mnth.index.strftime('%b')
	df_ret_mnth = df_ret_mnth.pivot('Year', 'Month', 'Returns').fillna(0)
	df_ret_mnth = df_ret_mnth[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
	size = list(plt.gcf().get_size_inches())
	figsize = (size[0], size[0] // 2)
	plt.close()
	#Create subplot
	fig, ax = plt.subplots(figsize=figsize)
	#create heatmap
	ax = sns.heatmap(df_ret_mnth, ax=ax, annot=True,
					 annot_kws={"size": 10}, fmt="0.2f", linewidths=0.5,
					 square=False, cbar=True, cmap='RdYlGn')
	ax.set_title('Monthly Returns (%)', fontsize=12, color='black', fontweight="bold")

	fig.subplots_adjust(hspace=0)
	plt.yticks(rotation=0)
	plt.show()
	plt.close()
















datapath="E:/sublime/assignment/Data cleaning/acc_test1.csv"
datapath2="E:/sublime/assignment/Data cleaning/accdaily1.csv"

if __name__=="__main__":
	cerebro=bt.Cerebro()
	cerebro.addstrategy(breakout)
	# cerebro.optstrategy(mystrategy,exitbars=range(5,10))
	data=bt.feeds.GenericCSVData(
	dataname=datapath,
	fromdate=dt.datetime(2018,1,2),
	todate=dt.datetime(2021,4,10),
	datetime=0,
	timeframe=bt.TimeFrame.Minutes,
	compression=1,
	dtformat=("%Y-%m-%d %H:%M:%S"),
	open=1,
	high=2,
	low=3,
	close=4,
	openinterest=-1,
	volume=5,
	reverse=False,
	header=0
		)
	
	data1=bt.feeds.GenericCSVData(
	dataname=datapath2,
	fromdate=dt.datetime(2018,1,1),
	todate=dt.datetime(2021,4,10),
	datetime=0,
	timeframe=bt.TimeFrame.Days,
	compression=1,
	dtformat=("%Y-%m-%d"),
	open=1,
	high=2,
	low=3,
	close=4,
	openinterest=-1,
	volume=5,
	reverse=False,
	header=0
		)

	
cerebro.adddata(data)
cerebro.adddata(data1)
cerebro.broker.setcash(1000000.00)
cerebro.addsizer(bt.sizers.FixedSize,stake=1)

cerebro.addanalyzer(bt.analyzers.TimeReturn,_name="TR",timeframe=bt.TimeFrame.Months)
print("Starting portfolio value :",cerebro.broker.getvalue())
res = cerebro.run()
tmereturn = res[0].analyzers.TR.get_analysis()
PrintTimeReturn(tmereturn)

# returns,positions, transactions, gross_lev = res[0].analyzers.pyfolio.get_pf_items()

# print(pd.DataFrame(returns))
# print(pd.DataFrame(positions))
# print(pd.DataFrame(transactions))
# print(pd.DataFrame(gross_lev))

print("Final portfolio value :",cerebro.broker.getvalue())