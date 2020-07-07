import time
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Your user agent'
}


class Main:

    def __init__(self):
        self.get_url()

    def get_url(self):
        # get URL
        self.url =  "https://shop.gadgetsnow.com/smartphones/samsung-galaxy-m30-32gb-metallic-blue-3gb-ram-/10021/p_G132498"
        self.check_price()

    # check price
    def check_price(self):
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # validate url page if item exists
        try:
            self.title = soup.find(class_='flt productcolumone zur').get_text().strip()
            self.price = soup.find(class_='offerprice flt').
        except:
            print('~' * 150)
            print('Error with URL , Copy Correct URL, Try Again !!')
            print('~' * 150)
            self.get_url()
        # strip_price = price[1:]
        # self.price = int(raw_price.replace(',', ''))

        print('Product Name: ', self.title)
        print('Reliance Product Price: ', self.price)


# call Class
Main()