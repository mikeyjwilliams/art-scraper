from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


class Browser:
    def __init__(self, driver):
        self.driver = driver

    def browser(self):

        self.driver = webdriver.Chrome()
        return self.driver

    def close_browser(self):

        self.driver.close()
        self.driver.quit()
