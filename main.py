from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from utils.Data import BASE_URL

from utils.browser import Browser
from utils.utility import close_iframe
from pages.homepage import HomePage


results = []
shirt_title_results: list = []
artist_name_results: list = []
sales_price_results: list = []
main_screen = None


def search():

    web_open = Browser(driver=Browser)
    runner = web_open.browser()
    runner.get(BASE_URL)
    sleep(3)
    web_open.close_browser()


if __name__ == '__main__':
    search()
    # HomePage.search()
