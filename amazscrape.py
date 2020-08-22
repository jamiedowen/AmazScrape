#Define imported packages
import requests
from bs4 import BeautifulSoup

#Define product URL, user agent and wanted price
URL = "https://www.amazon.co.uk/dp/B081QZPSG8/ref=dp_cerb_2"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
WANTED_PRICE = 810

def trackPrice():
    price = int(getPrice())
    if price > WANTED_PRICE:
        diffhigh = price - WANTED_PRICE
        print(f"Waiting for item to reach £{WANTED_PRICE}")
        print(f"It's still £{diffhigh} too expensive today")
    else:
        difflow = WANTED_PRICE - price
        print(f"It's £{difflow} cheaper than £{WANTED_PRICE} today")

#Request
def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()[1:4]
    print(title)
    print("Current Price: £",price, sep='')
    return price


if __name__ == "__main__":
    trackPrice()

