""" 2018-02-08 Sell executed 1589.85,2018-02-27 Buy executed 1655.0"""
import pandas as pd 
df = pd.read_csv("E:/sublime/assignment/Data cleaning/accdaily1.csv")
# print(df)
def naive_momentum_trading(financial_data, nb_conseq_days):
	signals = pd.DataFrame(index=financial_data.index)
	signals['orders'] = 0
	cons_day=0
	prior_price=0
	init=True
	for k in range(len(financial_data['close'])):
		price=financial_data['close'][k]
		if init:
			prior_price=price
			init=False
		elif price>prior_price :
			if cons_day<0:
				cons_day=0
				cons_day+=1
		elif price<prior_price:
			if cons_day>0:
				cons_day=0
				cons_day-=1
		if cons_day==nb_conseq_days:
			signals['orders'][k]=1
		elif cons_day == -nb_conseq_days:
			signals['orders'][k]=-1
	return signals
ts=naive_momentum_trading(df, 5)
ts.to_csv("E:/Backtest project/Naive_trading strategy/output.csv")