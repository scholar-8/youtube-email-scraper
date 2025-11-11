thonimport requests
from bs4 import BeautifulSoup
import csv
import time
import json

def fetch_emails(query, location, country, domain=None):
    search_url = f"https://www.google.com/search?q=site:youtube.com+{query}+{location}+{country}"
    if domain:
        search_url += f"+{domain}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    emails = set()
    for link in soup.find_all('a', href=True):
        if 'mailto:' in link['href']:
            emails.add(link['href'].split(':')[1])
    return list(emails)

def main():
    query = "jobs"
    location = "New York"
    country = "USA"
    domain = None  # or provide a custom domain like "@domain.com"
    
    emails = fetch_emails(query, location, country, domain)
    
    # Export to CSV
    with open("emails.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Profile URL", "Keyword", "Location", "Country"])
        for email in emails:
            writer.writerow([email, "N/A", query, location, country])

if __name__ == "__main__":
    main()