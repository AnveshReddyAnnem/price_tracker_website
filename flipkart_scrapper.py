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
        self.url = input('Enter Flipkart URL: ')
        # Splitting or slicing url to get website name i.e flipkart
        check_url = self.url.split("//")[-1].split("/")[0]
        # check if url belongs to Flipkart
        if check_url == 'www.flipkart.com':
            self.check_price()
        else:
            print('-' * 150)
            print(" You Seem to Have Entered Wrong URL. Check If Your is From Flipkart.com")
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
            self.title = soup.find(class_='_35KyD6').get_text()
            raw_price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()[1:]

        except:
            print('~' * 150)
            print('Error with URL , Copy Correct URL, Try Again !!')
            print('~' * 150)
            self.get_url()
        # strip_price = price[1:]
        self.price = int(raw_price.replace(',', ''))

        print('Product Name: ', self.title)
        print('Product Flipkart Price: ', self.price)


# call Class
Main()