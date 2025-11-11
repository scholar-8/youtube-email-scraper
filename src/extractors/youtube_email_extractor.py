thonimport requests
from bs4 import BeautifulSoup
import logging

class YouTubeEmailExtractor:
    def __init__(self, settings):
        self.settings = settings
        self.base_url = "https://www.google.com/search?q=site:youtube.com+email+{keyword}+{location}+{country}"
    
    def build_search_url(self, keyword, location, country):
        return self.base_url.format(keyword=keyword, location=location, country=country)

    def extract_emails(self):
        emails = []
        for keyword in self.settings['keywords']:
            for location in self.settings['locations']:
                for country in self.settings['countries']:
                    search_url = self.build_search_url(keyword, location, country)
                    response = requests.get(search_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        email_links = soup.find_all('a', href=True)
                        for link in email_links:
                            email = self.extract_email_from_link(link['href'])
                            if email and email not in emails:
                                emails.append(email)
        return emails

    def extract_email_from_link(self, link):
        if "mailto:" in link:
            return link.split("mailto:")[1]
        return None