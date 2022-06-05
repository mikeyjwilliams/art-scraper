from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.firefox.service import Service  # firefox service
from webdriver_manager.firefox import GeckoDriver  # firefox browser
from selenium.webdriver.chrome.service import Service  # chrome service
from webdriver_manager.chrome import ChromeDriverManager  # chrome browser

# ENVIRONMENTAL VARIABLES
from ENV import env

#   element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))

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
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # url
    driver.get('https://www.google.com')

    dismiss_popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'QlyBfb'))
    )
    dismiss = dismiss_popup.find_element(By.TAG_NAME, 'button')
    dismiss.click()

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf gsfi"))
    )
    search_input.send_keys('robot art')

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, 'QCzoEc z1asCe MZy1Rb'))
    )
    search_button.send_keys(Keys.ENTER)
    # driver.switchTo().alert().dismiss()
    # sleep(10)

    # driver.quit()


redbubble_search()
