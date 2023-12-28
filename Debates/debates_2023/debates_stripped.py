import sys
import debates_sorted

class Debates_stripped:
	'''strip the debatess from a Debates_sorted object, leaving only the indices'''
	
	def __init__(self, pd_srt):
	
		def strip_row(row):
			'''condense a list of index-debates pairs into a list of just the indices'''
			stripped_row = [row[0][0]]
			for j_col in range(1, len(row)):
					stripped_row += [row[j_col][0]]
			return stripped_row
		
		def strip_array(pd_srt):
			''' Return an array where each row is reduced to one list'''
			ar_stripped = [strip_row(pd_srt.pd_sorted[0])]
			for i_row in range(1, len(pd_srt.pd_sorted)):
					ar_stripped.append(strip_row(pd_srt.pd_sorted[i_row]))
			return ar_stripped
    
		#--main--------------------------------------------------------------------	
		if type(pd_srt) != debates_sorted.Debates_sorted:
			print( "debates_stripped: You must supply a Debates_sorted object.", 
					file=sys.stderr)
			exit(1)
	
		self.n_candidates = pd_srt.n_candidates
		self.n_debates = pd_srt.n_debates
		self.pd_stripped = strip_array(pd_srt)

	def print(self):
		print("debates_stripped:")
		print("[", end='')
		print(self.pd_stripped[0])
		for i_row in range(1, len(self.pd_stripped)-1):
			print("", self.pd_stripped[i_row])
		print("", self.pd_stripped[-1], end='')
		print("]")
