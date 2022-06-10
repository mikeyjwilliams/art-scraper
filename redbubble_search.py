from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# ENVIRONMENTAL VARIABLES
# from ENV import env

#   element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
# )
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present


def redbubble_search():
    url = 'https://www.redbubble.com'

    binary = FirefoxBinary('drivers/geckodriver.exe')
    driver = webdriver.Firefox(firefox_binary=binary)

    driver.get(url)
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'query'))
    )
    search_input.click()
    # url

    sleep(3)
    driver.quit()


redbubble_search()
