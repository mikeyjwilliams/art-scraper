from time import sleep
from utils.Data import BASE_URL
from utils.utility import Base


'''
homepage.py
goes to home page
checks its on home page
'''


class HomePage(Base):
    def __init__(self, driver):
        super.__init__(self, driver)

        driver = browser()
        driver.get(BASE_URL)
        sleep(3)
        driver.close_browser()
