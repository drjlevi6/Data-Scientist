import sys
import debates_array

class Debates_indexed:
	'''Turn a Debates_array object's entries into pairs: first item is entry's index in its row'''

	def __init__(self, pda):
		if type(pda) != debates_array.Debates_array:
			print( "debates_indexed: You must supply a Debates_array object.", file=sys.stderr)
			exit(1)

		ar = pda.ar
		self.n_candidates = pda.n_candidates
		self.n_debates = pda.n_debates
		
		self.pda_idx = []
		
		for i_row in range(self.n_debates):
			self.pda_idx.append([])
			for j_col in range(self.n_candidates):
				self.pda_idx[i_row].append([j_col+1, ar[i_row][j_col]])

	def print(self):
		print("\nDebates_indexed:")
		for i_row in range(self.n_debates):
			print("[", end=" ")
			for j_col in range(self.n_candidates):
				print("[{0:d}, {1:8.5f}]".format(*self.pda_idx[i_row][j_col]), end="")
				print(", " if j_col < self.n_candidates-1 else "", end="")
			print(" ]")