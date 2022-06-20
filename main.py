from time import sleep
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from utils.Data import BASE_URL

from utils.browser import browser, close_browser
from utils.utility import close_iframe
from pages.result import RedBubbleResultPage

chromedriver_autoinstaller.install()
results = []
shirt_title_results: list = []
artist_name_results: list = []
sales_price_results: list = []
main_screen = None


def search():

    driver = browser()
    driver.get(BASE_URL)
    sleep(3)
    close_browser(driver=driver)


if __name__ == '__main__':
    search()
