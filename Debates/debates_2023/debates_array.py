class Debates_array:
	'''Create (n_debates x n_candidates) array'''
	''' The array has the following properties:
			• the entries are created randomly;
			• no entry appears twice in a given row.
	'''
	def __init__(self, n_candidates=3, n_debates=4):
		self.n_candidates = n_candidates
		self.n_debates = n_debates
		
		def pushdown(x):
			return randint(0, 15) + x/16	# Divide by 16 to shift the number 1 hex 
																		# place to right without rounding errors.
		import random
		from random import randint
		
		self.ar = [[]]
		self.ar[0] = [x for x in range(n_candidates)]	

		for i in range(1, n_debates):
			self.ar.append([pushdown(x) for x in self.ar[i-1]])
	
	def print(self):
		print("\nDebates_array:")		
		# Create a format string for the rows
		format_string = '['
		for i in range(self.n_candidates-1):
			format_string += '{' + str(i) + ':8.5f} '
		format_string += '{' + str(self.n_candidates-1) + ':8.5f} ]'
		
		for row in self.ar:
			print(format_string.format(*row))
