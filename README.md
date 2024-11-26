# Web-Email-Extractor
This Python script is designed to scrape email addresses from a given website URL and its linked pages. The tool collects emails while navigating through URLs and saves them in a file.

---

## Features
- Scrapes email addresses from a target website.
- Crawls linked pages up to a limit of 100 URLs to prevent excessive requests.
- Handles common network errors gracefully.
- Outputs scraped emails to a text file for later use.

---

## Prerequisites
Ensure you have Python 3 installed along with the necessary dependencies. Install the required packages using `pip`.

---

## Installation
1. Clone the repository or download the script.
2. Navigate to the script's directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the script:
   ```bash
   python email_scraper.py
   ```
2. Enter the target website URL when prompted (e.g., `https://example.com`).
3. The script will process the pages and output the emails to `scraped_emails.txt` in the same directory.

---

## Notes
- The script supports both HTTP and HTTPS URLs.
- Results are limited to a maximum of 100 URLs to prevent abuse.
- Use responsibly and respect website terms of service.

---

## Example
```plaintext
$ python email_scraper.py
[+] Enter Target URL To Scan: https://example.com
[1] Processing https://example.com
[2] Processing https://example.com/contact
[3] Processing https://example.com/about
...
[+] Emails successfully scraped. Results saved in 'scraped_emails.txt'.
```

---

## Troubleshooting
- **No emails found:** Ensure the target website contains visible email addresses.
- **Network errors:** These may occur if the website blocks your IP or experiences downtime.
- **Invalid URL:** Ensure the URL includes `http://` or `https://`.

---

## Disclaimer
This tool is for educational and ethical use only. Unauthorized scraping of websites may violate their terms of service. Always obtain permission before scraping.

---

This structured documentation ensures the script's usage is clear and provides all necessary details.
