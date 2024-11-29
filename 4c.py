import requests
from bs4 import BeautifulSoup

# URL of the blog homepage
url = 'https://example.com/blog'  # Replace with the actual blog URL

# Fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract article titles (h2 tags with class 'article-title')
titles = soup.find_all('h2', class_='article-title')

# Print each title
for title in titles:
    print(title.get_text())