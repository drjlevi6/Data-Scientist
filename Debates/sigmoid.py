'''Compute sigmoid curves connecting two endpoints'''

import math
import pandas as pd
from pandas import DataFrame

class Sigmoid:
	'''Interpolate points in a sigmoid pattern between start-, end points'''
	def __init__(self):
		self.x_start = None
		self.y_start = None
		self.x_end = None
		self.y_end = None
		self.x_mid = None
		self.L = None
		self.k = None
		self.num_points = None

	def compute_logistic_points(self, x_start, y_start, x_end, y_end,
		num_points=100):
		'''Compute list of (num_points) pairs [x, logistic(x)]'''
		self.x_start = x_start
		self.y_start = y_start
		self.x_end = x_end
		self.y_end = y_end
		self.x_mid = (self.x_start + self.x_end) / 2
		self.L = self.y_end - self.y_start
		self.k = -12 / (self.x_start - self.x_end)
		
		output = []
		for n in range(num_points):
			x = x_start + ( (x_end - x_start) * n / (num_points-1))
			output.append([x, self.logistic(x)])
		return output
	
	def logistic(self, x):
		'''Compute logistic function f(x)'''
		'''Logistic curve:
				f(x) = L / (1 + exp(-k(x-x0)) )
			where
				x0 = x-value of the function's midpoint;
				L = the supremum of the values of the function;
				k = logistic growth rate or steepness of the curve
			(here, k is set such that for start- and endpoints [-1, -1] and [1, 1],
				f(1) > 0.99)		
			Ref: https://en.wikipedia.org/wiki/Logistic_function
		'''
		return self.y_start + self.L / (1 + math.exp(-self.k * (x - self.x_mid)))
	
	def compute_logistic_dataframe(self, x_start, y_start, x_end, y_end,
		num_points=100):
		'''return a pandas dataframe, data computed by compute_logistic_points()'''
		return DataFrame(self.compute_logistic_points(x_start, y_start, x_end,
			y_end, num_points))
	
	def compute_logistic_dataframe_one_row(self, x_start, y_start, x_end, y_end,
		num_points=100):
		'''return pd dataframe of one row, data computed by compute_logistic_points()'''
		df = self.compute_logistic_dataframe(x_start, y_start, x_end, y_end,
			num_points)
		return DataFrame(df[1])