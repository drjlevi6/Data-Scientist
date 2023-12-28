import sys
import debates_indexed

class Debates_sorted:
	'''sort rows of a debates_indexed object by increasing order of the values'''
	
	def __init__(self, pd_idx):

		def make_new_row(i_row):
			old_row = pd_idx.pda_idx[i_row]
			new_row  = [0] * self.n_candidates
		
			row_vals = [pd_idx.pda_idx[i_row][j_col][1] for j_col in range(self.n_candidates)]
			row_vals_sorted = sorted(row_vals)

			for j_col in range(self.n_candidates):
				new_index = row_vals.index(row_vals_sorted[j_col])
				new_row[j_col] = old_row[new_index]

			return new_row

		#--main--------------------------------------------------------------------	
		if type(pd_idx) != debates_indexed.Debates_indexed:
			print( "debates_indexed: You must supply a Debates_indexed object.", 
				file=sys.stderr)
			exit(1)
			
		self.n_candidates = pd_idx.n_candidates
		self.n_debates = pd_idx.n_debates
		self.pd_sorted = [1] * self.n_debates 
				
		for i_row in range(self.n_debates):
			self.pd_sorted[i_row] = make_new_row(i_row)

	def print(self):
		print("\ndebates_sorted:")
		for i_row in range(self.n_debates):
			print("[", end=" ")
			for j_col in range(self.n_candidates):
				print("[{0:d}, {1:8.5f}]".format(*self.pd_sorted[i_row][j_col]), end="")
				print(", " if j_col < self.n_candidates-1 else "", end="")
			print(" ]")			
			
		