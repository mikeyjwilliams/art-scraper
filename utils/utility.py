from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


URL: str = 'https://www.redbubble.com'


class Browsers:

    def __init__(self):
        self.browser = webdriver.Firefox

    def firefox_browser_open(self):
        driver = self.browser(
            service=Service(GeckoDriverManager().install()))
        driver.implicitly_wait(3)

        # return the driver object at the end of setup.
        driver.get(URL)

    def close_browser(self):
        self.browser.close()
        self.browser.quit()
