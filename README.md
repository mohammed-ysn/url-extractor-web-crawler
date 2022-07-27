# URL Extractor Web Crawler

This program is a web crawler that outputs URLs that a source website links to (directly or indirectly).

Direct link: there are no intermediate websites between the source and target websites.

Indirect link: there is at least one intermediate website between the source and target websites.

## Run the Crawler
The `requirements.txt` file contains all Python libraries that the program
depends on. Install them using:

```
pip install -r requirements.txt
```

In `run.py`, enter your desired start URL (`start_url`) as well as the target number of URLs the scraper is to extract (`target_number_of_urls`).

Run `run.py`.