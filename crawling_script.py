import requests
from bs4 import BeautifulSoup

# Set the URL of the website to crawl
# url = "https://www.example.com"
url = "http://nemis.education.go.ke/"

# Send a request to the website and get its HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Print the links found on the page
for link in links:
    href = link.get("href")
    if href is not None:
        print(href)
