from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
import os


def email_scraper():
    print("[+] Email Scraper Tool")
    user_url = input("[+] Enter Target URL To Scan: ").strip()
    if not user_url.startswith("http://") and not user_url.startswith("https://"):
        print("[-] Invalid URL. Please include 'http://' or 'https://' in the URL.")
        return

    urls = deque([user_url])
    scraped_urls = set()
    emails = set()

    count = 0
    try:
        while len(urls):
            count += 1
            if count > 100:  # Limit to prevent excessive requests
                print("[!] URL processing limit reached (100). Exiting.")
                break

            url = urls.popleft()
            scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = f"{parts.scheme}://{parts.netloc}"
            path = url[: url.rfind("/") + 1] if "/" in parts.path else url

            print(f"[{count}] Processing {url}")
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # Raise HTTP errors
            except requests.exceptions.RequestException as e:
                print(f"[!] Error fetching {url}: {e}")
                continue

            # Extract emails with improved filtering
            new_emails = set(
                re.findall(
                    r"[a-zA-Z0-9.\-+_]+@[a-zA-Z0-9.\-+_]+\.[a-zA-Z]+",
                    response.text,
                    re.I,
                )
            )
            for email in new_emails:
                # Exclude common image formats and invalid email patterns
                if not email.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".gif", ".webp")
                ):
                    emails.add(email)

            soup = BeautifulSoup(response.text, features="lxml")
            for anchor in soup.find_all("a", href=True):
                link = anchor["href"]
                if link.startswith("/"):
                    link = base_url + link
                elif not link.startswith("http"):
                    link = path + link
                if link not in urls and link not in scraped_urls:
                    urls.append(link)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting...")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

    if emails:
        output_file = "scraped_emails.txt"
        with open(output_file, "w") as f:
            for email in sorted(emails):
                f.write(email + "\n")
        print(f"[+] Emails successfully scraped. Results saved in '{output_file}'.")
    else:
        print("[-] No emails found.")


if __name__ == "__main__":
    email_scraper()
