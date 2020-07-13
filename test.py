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
        self.url =  "https://www.tatacliq.com/apple-iphone-11-64-gb-green/p-mp000000005562295"
        self.check_price()

    # check price
    def check_price(self):
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # validate url page if item exists
        try:
            self.title = soup.find('h1', attrs={'class':'_2qfozlUZGLD1nRgcHNLXdP'}).get_text()
            self.price = soup.find('h1', attrs={'class':'_3BuuEa4DZJe-0OCEQmi_K_'}).get_text()
        except:
            print('~' * 150)
            print('Error with URL , Copy Correct URL, Try Again !!')
            print('~' * 150)
            self.get_url()
        # strip_price = price[1:]
        # self.price = int(raw_price.replace(',', ''))

        print('Product Name: ', self.title)
        print('TATA Product Price: ', self.price)


# call Class
Main()