from re import I
from time import sleep

from selenium import webdriver
from utils.Data import BASE_URL
from utils.utility import Base

from utils.browser import browser
from utils.browser import close_browser

'''
homepage.py
goes to home page
checks its on home page
'''


class HomePage(Base):
    def __init__(self, driver):
        super.__init__(self, driver)

    pass
