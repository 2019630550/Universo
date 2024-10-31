import requests
from bs4 import BeautifulSoup
import webbrowser

url = "https://concepto.de/fisica/"

webbrowser.open(url)

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.title

print(title)