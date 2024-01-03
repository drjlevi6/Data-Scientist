'''Prompt user to paste URL containing the transcript from the browser'''
def get_url_from_user():
	'''Print prompt to stderr to avoid including it in output'''
	import sys
	print("Paste the URL containing your transcript from your browser:", file=sys.stderr)
	return input()