import pandas as pd
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objs as go
from sigmoid import Sigmoid
import debates_stripped
import debates_df_displayer

print("debates_with_sigmoids: __name__:", __name__)

class Debates_with_sigmoids:
	'''Convert stripped array to dataframe with interpolated sigmoids; display'''

	def __init__(self, pd_strip, linewidth=60):
		self.pd_strip = pd_strip
		self.df = DataFrame(pd_strip.pd_stripped)
		self.s = None
		self.linewidth = linewidth

	def make_sigmoid_df(self, j_col):
		x, y = [], []
		for i in range(self.df.shape[0]-1):
			pts = self.s.compute_logistic_points(i, self.df.iloc[i,j_col], 
				i+1, self.df.iloc[i+1,j_col])
			x += [p[0] for p in pts]
			y += [p[1] for p in pts]
		df_indexed = DataFrame({"x": x, "y": y}).set_index("x")
		return df_indexed

	def show(self):
		self.s = Sigmoid()
		
		df_sigmoids = []	# dataframes for each column of the original dataframe;
											# new dataframes contain interpolated sigmoid curves
		for j_col in range(self.df.shape[1]):
			df_sigmoids.append(self.make_sigmoid_df(j_col))

		fig = px.line(title="The Great Republican Debate: Results")
		traces = []
		for i in range(len(df_sigmoids)):
			dfs = df_sigmoids[i]
			values_list = [v[0] for v in dfs.values]
			traces.append(go.Scatter(x=dfs.index, y=values_list, 
									line={"width": self.linewidth},
									name=("Candidate " + str(i))))

		for t in traces:
			fig.add_trace(t)

		fig.update_layout(
			xaxis = dict(tickmode = 'linear', tick0 = 1, dtick = 1, 
						 title="Debate Number"),
			yaxis = dict(tickmode = 'linear', tick0 = 1, dtick = 1, 
						 title="Rank after Debate"),
		)
		fig.show()
