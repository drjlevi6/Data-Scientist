from .get_url import get_url_from_user
from .transcript_scraper import get_transcript

if __name__ != '__main__':
	url = get_url_from_user()
	get_transcript(url)
else:
	import transcript_scraper