import os
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

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

results = []


def redbubble_search():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    url: str = 'https://www.redbubble.com'
    key_phrase: str = 'robot art'

    driver.get(url)

    search_query = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'query'))
    )
    search_query.click()
    search_query.send_keys(key_phrase)

    search_query.send_keys(Keys.ENTER)
    # driver.switchTo().alert().dismiss()

    title_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'SearchResults'))
    )
    results.append(title_text.text)

    sleep(3)

    driver.quit()


redbubble_search()


sleep(1)
print('---------------')
print('my findings are.')
for finds in results:
    print(finds)
