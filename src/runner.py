thonimport os
import json
import logging
from extractors.youtube_email_extractor import YouTubeEmailExtractor
from outputs.exporters import CSVExporter, ExcelExporter

logging.basicConfig(level=logging.INFO)

def load_settings():
    try:
        with open('src/config/settings.example.json', 'r') as file:
            settings = json.load(file)
        return settings
    except Exception as e:
        logging.error(f"Error loading settings: {e}")
        return {}

def run_scraper(settings):
    extractor = YouTubeEmailExtractor(settings)
    emails = extractor.extract_emails()
    
    if emails:
        CSVExporter().export(emails, "emails_output.csv")
        ExcelExporter().export(emails, "emails_output.xlsx")
        logging.info("Data exported successfully.")
    else:
        logging.warning("No emails found.")

if __name__ == "__main__":
    settings = load_settings()
    if settings:
        run_scraper(settings)