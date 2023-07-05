import requests
from bs4 import BeautifulSoup

def getPost(url):
    response = requests.get(url)
    soup     = BeautifulSoup(response.content, "html.parser")
    title    = soup.find("h1").text
    paragraphs = soup.find_all("p")

    text = ""

    for p in paragraphs:
        text += p.get_text()

    return text, title