# transcript_scraper

Scrape transcripts from LinkedIn Learning course lectures

### Description

This Python package is designed to scrape the transcript from a LinkedIn Learning course lecture. When run, it prompts the user for the URL of the course lecture, then scrapes all of (or part of: see "Bugs" below) the lecture's transcript, including its header, and prints them to stdout.

### Usage

`python -m transcript_scraper`

You will be prompted to enter the URL whose transcript is to be scraped.

### Dependencies

* The `requests` package
* `BeautifulSoup` from the `bs4` package

(Do `pip install requests` and/or `pip install bs4` as needed)

### Bugs

On some occasions transcript_scraper prints an incomplete transcript. This does not seem to be related to the transcript's length. The cause is undetermined.