import requests
from bs4 import BeautifulSoup
import time

def excheng(fram, to, amount):
    sait = f"https://www.x-rates.com/calculator/?from={fram}&to={to}&amount={amount}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    full_page = requests.get(sait, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "ccOutputRslt"})
    return convert[0].text

excheng("EUR", "RUB", 100)
