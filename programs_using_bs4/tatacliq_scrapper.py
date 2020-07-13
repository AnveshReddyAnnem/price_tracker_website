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
        self.url = input('Enter TataCliq url: ')
        # Splitting or slicing url to get website name i.e Amazon.in
        check_url = self.url.split("//")[-1].split("/")[0]
        # check if url belongs to Amazon.in
        if check_url == 'www.tatacliq.com':
            self.check_price()
        else:
            print('-' * 150)
            print(" You Seem to Have Entered Wrong URL. Check If Your is From tatacliq.com")
            print('-' * 150)
            time.sleep(2)
            # if wrong url re-run get_url()
            self.get_url()

    # check price
    def check_price(self):
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # validate url page if item exists
        try:
            # self.title = soup.select("#productTitle")[0].get_text().strip()
            self.title = soup.find(class_='_2qfozlUZGLD1nRgcHNLXdP').get_text()
            # self.price = soup.select("#priceblock_ourprice")[0].get_text()
            self.price = soup.find(class_='_3BuuEa4DZJe-0OCEQmi_K_').find('h3')
        except:
            print('~' * 150)
            print('Error with URL , Copy Correct URL, Try Again !!')
            print('~' * 150)
            self.get_url()
        # strip_price = price[1:]
        # self.price = int(raw_price.replace(',', ''))

        print('Product Name: ', self.title)
        print('Amazon Product Price: ', self.price)


# call Class
Main()