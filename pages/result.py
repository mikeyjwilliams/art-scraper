from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class RedBubbleResultPage:
    LINK_DIVS = (By.CSS_SELECTOR, '#SearchResultsGrid > a')
    SEARCH_BAR = (By.TAG_NAME, 'input')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//input//*[contains(text(),'{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(
            *self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    def search_input_value(self):
        search_bar = self.browser.find_element(*self.SEARCH_BAR)
        return search_bar.get_attribute('value')
