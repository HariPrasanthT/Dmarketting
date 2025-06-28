from scraper import extract_emails_and_names
from utils import save_to_excel, save_to_txt_table

def is_valid_lead(name_list):
    for name in name_list:
        if "entrepreneur" in name.lower():
            return True
    return False


def main():
    urls = input("Enter URLs separated by commas: ").split(",")
    urls = [url.strip() for url in urls]

    country_filter = input("Enter country filter (optional): ").lower()

    leads = []

    for url in urls:
        print(f"[+] Scraping: {url}")
        emails, names = extract_emails_and_names(url)

        if is_valid_lead(names):
            lead_data = {
                "Website URL": url,
                "Emails": ", ".join(emails) if emails else "N/A",
                "LinkedIn Names": ", ".join(names) if names else "N/A",
                "Country": country_filter.title() or "Unknown"
            }

            if "http" in url and not re.search(r"\.(com|net|org|in|co|io)", url.split("//")[1]):
                continue  # skip websites with domain names

            leads.append(lead_data)

    if not leads:
        print("No valid leads found.")
        return

    save_to_excel(leads)
    save_to_txt_table(leads)

if __name__ == "__main__":
    main()
