'''Get text of LinkedIn Learning courses' transcripts'''
import requests
from bs4 import BeautifulSoup
import re

def get_transcript_header(url):
	'''Attempt to limit body text, else requests.text may return an incomplete result'''
	results = requests.get(url, params={'class': 'core-section-container__title'})	
	soup = BeautifulSoup(results.text, "lxml")
	return soup
	
def get_transcript_body(url):
	results = requests.get(url)	
	soup = BeautifulSoup(results.text, "lxml")
	return soup

def get_transcript(url):
	'''Attempt to limit body text, else requests.text may return an incomplete result'''

	# "Prettify" and merge header, body
	header_soup = get_transcript_header(url)
	transcript_header = header_soup.find("h2", attrs={'class': 'core-section-container__title'})
	transcript_header_text = list(transcript_header)[0].strip()

	body_soup = get_transcript_body(url)
	transcript_body = body_soup.find("div", attrs={'class': 'transcripts__copy'})
	transcript_body_text_unformatted = list(transcript_body.stripped_strings)[1]
	transcript_body_text = re.sub('\ \ +', ' ', transcript_body_text_unformatted)

	# Eliminate initial, final and redundant spaces
	print(transcript_header_text, '\n', transcript_body_text)
	
if __name__ == '__main__':
	sample_url = 'https://www.linkedin.com/learning/' + \
		'python-for-data-science-essential-training-part-1/navigablestring-objects'
	get_transcript(sample_url)
	