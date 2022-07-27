import requests
import validators
from bs4 import BeautifulSoup


class UrlScraper:
    def __init__(self, start_url, n):
        self.start_url = start_url
        self.n = n

        # store all URLs yet to be explored
        self.frontier = []

        # store all unique URLs the scraper has found
        self.extracted_urls = set()

    def scrape_page(self, page_url):
        # convert page HTML to soup object
        page = requests.get(page_url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # locate all unique href values in <a> tags
        hrefs = {elem.get('href') for elem in soup.find_all('a')}

        # filter out non-urls from the hrefs
        urls_on_page = []
        for href in hrefs:
            if href is not None and validators.url(href):
                urls_on_page.append(href)

        for url in urls_on_page:
            if len(self.extracted_urls) == self.n:
                # target number of URLs has been reached
                break

            if url not in self.extracted_urls:
                # url has not been seen before
                self.frontier.append(url)

            self.extracted_urls.add(url)

    def extract_urls(self):
        self.frontier.append(self.start_url)

        # end loop when either:
        # - target number of URLs are found
        # - frontier is empty (all reachable URLs have been visited)
        while len(self.extracted_urls) < self.n and self.frontier:
            next_url = self.frontier.pop(0)
            print(f'Visiting: {next_url}')
            self.scrape_page(next_url)
