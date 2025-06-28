from flask import Flask, render_template, request
from scraper import extract_emails_and_names
from utils import save_to_excel, table_to_text
import re

app = Flask(__name__)

def is_valid_lead(name_list):
    for name in name_list:
        if any(keyword in name.lower() for keyword in ["entrepreneur", "ceo", "founder"]):
            return True
    return False

def has_website_in_url(url):
    return bool(re.search(r"\.(com|net|org|in|co|io|biz|site|me)", url.lower()))

@app.route("/", methods=["GET", "POST"])
def index():
    table = None

    if request.method == "POST":
        urls = request.form["urls"].splitlines()
        country_filter = request.form["country"].strip().lower()
        leads = []

        for url in urls:
            url = url.strip()
            if not url:
                continue

            emails, names = extract_emails_and_names(url)

            if not emails and not names:
                continue

            if has_website_in_url(url):
                continue

            if is_valid_lead(names):
                leads.append({
                    "Website URL": url,
                    "Emails": ", ".join(emails) if emails else "N/A",
                    "LinkedIn Names": ", ".join(names) if names else "N/A",
                    "Country": country_filter.title() or "Unknown"
                })

        if leads:
            save_to_excel(leads)
            table = table_to_text(leads)

    return render_template("index.html", table=table)

if __name__ == "__main__":
    app.run(debug=True)
