'''Test CSV-style RGB strings of pixels to see if they're gray'''
import re

def is_grayscale(s):
	''' Determine whether a CSV-string of integers could represent grayscale pixels'''
	
	# recognize triplets of identical ints one by one, else
	#  we get error "re.error: cannot refer to an open group...""	
	triplet_re = re.compile(r'(\d{1,3}),\1,\1')
	
	found = re.findall(triplet_re, s)
	
	triplets = [(found[i]+',')*3 for i in range(len(found))]
	reconstructed = ''.join(triplets)[:-1]
	return (reconstructed == s)

def main():
	'''Run function is_grayscale() on test strings if this module is run "freestanding"'''
	csv_strings = [
		'1',
		'1,1,1',
		'1,1,1,21,21,21',
		'1,1,1,21,21,21,',
		'1,2,1,21,21,21',
		'aaa',
		'-1,-1,-1',
		'1,1,1,1'
	]
	print("Testing sample strings as possible gray pixels:")
	for s in csv_strings:
		print('“' + s + "”:", is_grayscale(s))

def is_imported():
	'''Prompt user endlessly for strings; determine whether they could represent gray pixels'''
	while True:
		print("Enter comma-delimited ints to evaluate as gray pixels or " + \
			"press Return to quit:")
		try:
			s = input()
			if s == '':
				exit(0)
			print(is_grayscale(s))
		except Exception:
			exit(0)

if __name__ == "__main__":
	main()
else:
	is_imported()
