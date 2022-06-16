from time import sleep
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from utils.Data import BASE_URL


from utils.utility import close_iframe
from pages.result import RedBubbleResultPage

chromedriver_autoinstaller.install()
results = []
shirt_title_results: list = []
artist_name_results: list = []
sales_price_results: list = []
main_screen = None


def browser():

    driver = webdriver.Chrome()
    return driver


def close_browser(driver):

    driver.close()
    driver.quit()


driver = browser()
driver.get(BASE_URL)
sleep(3)
close_browser(driver=driver)
