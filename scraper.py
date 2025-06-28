from bs4 import BeautifulSoup
import requests
import re


def extract_emails_and_names(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract visible text
        text = soup.get_text()

        # Emails
        emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)))

        # Possible LinkedIn or personal names
        names = []
        for link in soup.find_all("a", href=True):
            if "linkedin.com/in" in link["href"]:
                names.append(link.text.strip())

        return emails, names

    except Exception as e:
        print(f"Error while scraping {url}: {e}")
        return [], []
a