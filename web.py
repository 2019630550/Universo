import requests
from bs4 import BeautifulSoup

url = "https://concepto.de/fisica/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.title

print(title)