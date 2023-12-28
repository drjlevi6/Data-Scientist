'''Display straight and rounded tables (dataframes) of candidates' rankings'''
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objs as go
import sys

def show(df):
	if type(df) != DataFrame:
			print( "debates_df_displayer: You must supply a DetaFrame object.", 
				file=sys.stderr)
			exit(1)

	fig = px.line(title="The Great Republican Debate: Results")
	traces = []
	for i in range(len(df)):
		dfs = df[i]
		values_list = [v[0] for v in dfs.values]
		traces.append(go.Scatter(x=dfs.index, y=values_list, 
								line={"width": 10},
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
