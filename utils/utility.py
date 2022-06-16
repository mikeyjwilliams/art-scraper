from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Browsers:

    def __init__(self, browser):
        self.browser = browser

    def firefox_browser(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        driver.implicitly_wait(3)

        # return the driver object at the end of setup.
        yield driver

        # for cleanup, quit the driver.
        driver.quit()
