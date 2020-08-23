# Based off Devscover's video https://www.youtube.com/watch?v=SyW6YK7ftis&list=WL&index=46&t=882s
#Define imported packages
import time
import requests
import smtplib
from bs4 import BeautifulSoup
from datetime import datetime

#Define product URL, user agent and wanted price
URL = "https://www.amazon.co.uk/dp/B081QZPSG8/ref=dp_cerb_2"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
WANTED_PRICE = 840
SENDER_EMAIL = "sender email"
DESTINATION_EMAIL = "destination email"

def trackPrice():
    price = float(getPrice())
    if price > WANTED_PRICE:
        diffHigh = price - WANTED_PRICE
        print(f"Waiting for item to reach £{WANTED_PRICE}")
        print(f"It's still £{diffHigh:1.2f} too expensive today")
    else:
        diffLow = WANTED_PRICE - price
        print(f"It's £{diffLow:1.2f} cheaper than £{WANTED_PRICE} today")
        sendMail()

#Request
def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()[1:7]
    print("Item:",title)
    print("Current Price: £",price, sep='')
    return price

def sendMail():
    subject = "Amazon price has dropped"
    mailtext = "Subject:"+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, 'password')
    server.sendmail(DESTINATION_EMAIL, DESTINATION_EMAIL, mailtext)
    pass

if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(60)

