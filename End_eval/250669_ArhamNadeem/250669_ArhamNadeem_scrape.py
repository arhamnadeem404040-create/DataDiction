from bs4 import BeautifulSoup
import pandas as pd
import os

# Path handling (safe)
BASE_DIR = os.path.dirname(__file__)
HTML_PATH = os.path.join(BASE_DIR, "end_eval.html")

# Open HTML file
with open(HTML_PATH, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find table
table = soup.find("table")

# Extract headers
headers = [th.text.strip() for th in table.find_all("th")]

# Extract rows
rows = []
for tr in table.find_all("tr")[1:]:
    cells = tr.find_all("td")
    rows.append([cell.text.strip() for cell in cells])

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save CSV
csv_path = os.path.join(BASE_DIR, "scraped_data.csv")
df.to_csv(csv_path, index=False)

print("Scraping complete. File saved as scraped_data.csv")
