import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.cabinc.com/steel-pipe-flanges")
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())