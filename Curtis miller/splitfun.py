from sklearn.model_selection import TimeSeriesSplit
from sklearn.utils import indexable
from sklearn.utils.validation import _num_samples
import numpy as np
class TimeSeriesSplitImproved(TimeSeriesSplit):

	def split(self, X, y=None, groups=None, fixed_length=False, train_splits=1, test_splits=1):
		X, y, groups = indexable(X, y, groups)
		n_samples = _num_samples(X)
		n_splits = self.n_splits
		n_folds = n_splits + 1
		train_splits, test_splits = int(train_splits), int(test_splits)
		if n_folds > n_samples:
			raise ValueError(
				("Cannot have number of folds ={0} greater"
				 " than the number of samples: {1}.").format(n_folds,
															 n_samples))
		if (n_folds - train_splits - test_splits) <  0 and test_splits > 0:
			raise ValueError(
				("Both train_splits and test_splits must be positive"
				 " integers."))
		indices = np.arange(n_samples)
		split_size = (n_samples // n_folds)
		test_size = split_size * test_splits
		train_size = split_size * train_splits
		test_starts = range(train_size + n_samples % n_folds,
							n_samples - (test_size - split_size),
							split_size)
		if fixed_length:
			for i, test_start in zip(range(len(test_starts)),
									 test_starts):
				rem = 0
				if i == 0:
					rem = n_samples % n_folds
				yield (indices[(test_start - train_size - rem):test_start],
					   indices[test_start:test_start + test_size])
		else:
			for test_start in test_starts:
				yield (indices[:test_start],indices[test_start:test_start + test_size])