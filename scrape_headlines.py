import requests
from bs4 import BeautifulSoup

# Step 1: Target URL
url = "https://www.bbc.com/news"

# Step 2: Send HTTP Request
response = requests.get(url)

# Step 3: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines
headlines = []

# BBC headlines are inside <h3> tags with specific classes
for h in soup.find_all("h3"):
    headline = h.get_text(strip=True)
    if headline and headline not in headlines:
        headlines.append(headline)

# Step 5: Save to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for line in headlines:
        file.write(line + "\n")

print("Scraping complete. Headlines saved to 'headlines.txt'.")
