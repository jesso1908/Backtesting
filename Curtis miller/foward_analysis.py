from splitfun import TimeSeriesSplitImproved
import pandas as pd 
import random
tscv = TimeSeriesSplitImproved(10)
data_1 = pd.read_csv("E:/sublime/assignment/Data cleaning/accdaily1.csv")
split = tscv.split(data_1, fixed_length=True, train_splits=2)

walk_forward_results = list()
for train,test in split:
	windowset = set()    # Use a set to avoid duplicates
	while len(windowset) < 40:
		f = random.randint(5, 10) 
		s = random.randint(15, 30)
		if f > s:    # Cannot have the fast moving average have a longer window than the slow, so swap
			f, s = s, f
		elif f == s:    # Cannot be equal, so do nothing, discarding results
			pass
		windowset.add((f, s))

windows = list(windowset)
	


