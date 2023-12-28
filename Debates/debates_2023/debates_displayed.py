import pandas as pd
from pandas import DataFrame
import plotly.express as px
import sys
import debates_stripped
import plotly.graph_objs as go

class Debates_displayed:
	'''Convert a debates_stripped array to pandas dataframe, display with plotly'''
	
	def __init__(self, pd_strip):
		'''Convert and display array'''
#		print("debates_displayed, pd_strip.pd_stripped:", pd_strip.pd_stripped)		
		fig = px.line(pd_strip.pd_stripped, title="The Great Republican Debate: Results")
		fig.update_layout(
			xaxis = dict(tickmode = 'linear', tick0 = 1, dtick = 1, 
						 title="Debate Number"),
			yaxis = dict(tickmode = 'linear', tick0 = 1, dtick = 1, 
						 title="Rank after Debate"),
		)
		fig.update_traces(line=dict(width=20))
		fig.show()
