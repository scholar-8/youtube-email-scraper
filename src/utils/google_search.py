thonimport requests
from bs4 import BeautifulSoup

def search_youtube_profiles(query, location=None, country=None, max_results=10):
    search_url = f"https://www.google.com/search?q=site:youtube.com+{query}"
    if location:
        search_url += f"+{location}"
    if country:
        search_url += f"+{country}"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for g in soup.find_all('div', class_='BVG0Nb'):
        link = g.find('a')['href']
        if "youtube.com" in link:
            links.append({"url": "https://www.google.com" + link})
            if len(links) >= max_results:
                break

    return links