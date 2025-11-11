thonimport csv
import requests
from bs4 import BeautifulSoup
from utils.google_search import search_youtube_profiles
from extractors.youtube_email_extractor import extract_email

def scrape_emails(query, location=None, country=None, email_type="both", max_results=10):
    profiles = search_youtube_profiles(query, location, country, max_results)
    emails = []

    for profile in profiles:
        email = extract_email(profile['url'], email_type)
        if email:
            emails.append({
                'email': email,
                'profileUrl': profile['url']
            })
    
    return emails

def save_to_csv(emails, filename="emails_sample.csv"):
    keys = emails[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(emails)

if __name__ == "__main__":
    query = "marketing"
    emails = scrape_emails(query)
    save_to_csv(emails)