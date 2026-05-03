import requests
from bs4 import BeautifulSoup

# Step 1: Fetch a web page
print("Fetching webpage...")
url = "https://example.com"
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an error for bad status codes
    print(f"✓ Successfully fetched {url}")
except requests.exceptions.RequestException as e:
    print(f"✗ Error fetching page: {e}")
    exit(1)

# Step 2: Parse the HTML
print("\nParsing HTML...")
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract the page title
title = soup.find('title')
if title:
    print(f"Page Title: {title.string}")
else:
    print("No title tag found")

# Step 4: Extract all hyperlinks
print("\nExtracting all links...")
links = soup.find_all('a', href=True)
print(f"Found {len(links)} links:\n")
for i, link in enumerate(links[:10], 1):  # Show first 10 links
    print(f"{i}. {link['href']}")
if len(links) > 10:
    print(f"... and {len(links) - 10} more links")

print("\n✓ Scraping complete!")