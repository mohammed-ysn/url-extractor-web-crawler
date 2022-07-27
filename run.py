from scraper import UrlScraper

if __name__ == '__main__':
    start_url = 'https://news.ycombinator.com/'
    target_number_of_urls = 100

    url_scraper = UrlScraper(start_url, target_number_of_urls)
    url_scraper.extract_urls()
    print(f'{len(url_scraper.extracted_urls)} urls found')
    for url in url_scraper.extracted_urls:
        print(url)
