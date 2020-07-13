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
        self.url = input('Enter RelianceDigital URL: ')
        # Splitting or slicing url to get website name i.e flipkart
        check_url = self.url.split("//")[-1].split("/")[0]
        # check if url belongs to Flipkart
        if check_url == 'www.reliancedigital.in':
            self.check_price()
        else:
            print('-' * 150)
            print(" You Seem to Have Entered Wrong URL. Check If Your is From www.reliancedigital.in")
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
            self.title = soup.find(class_='pdp__title').get_text()
            self.price = soup.find(class_='pdp__offerPrice').get_text()

        except:
            print('~' * 150)
            print('Error with URL , Copy Correct URL, Try Again !!')
            print('~' * 150)
            self.get_url()

        print('Product Name: ', self.title)
        print('Product RelianceDigital Price: ', self.price)


# call Class
Main()