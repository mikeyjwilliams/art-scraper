from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import Browser
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# custom imports


def close_iframe(browser):
    # closes iframe pop up box
    WebDriverWait(browser, 20).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, 'lightbox-iframe-9d8cb083-db92-488b-9101-eff3183f4a23'))
    )
    close_lightbox = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'button2'))
    )
    close_lightbox.click()

    browser.switch_to.parent_frame()


class Base:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        '''
        function: click
        description: locator variable decides where to click
        '''
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).click()

    def assert_el_text(self, locator, el_text):
        web_el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator))
        assert web_el == el_text

    def enter_text(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def search_input(self, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form[role='search'] input[type='text']")))

    def find_search_bar(self):
        '''
        function: find_search_bar
        Description: finds search bard by css selector `input` and search or text.
        Args:
            None
        Returns:
            found

        '''
        found = None
        input_search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"input [type='search']")))
        input_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"input [type='text']")))
        if input_search is True:
            found = input_search
        else:
            found = input_text
        return found
