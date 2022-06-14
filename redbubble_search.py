from time import sleep

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

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
shirt_title_results: list = []
artist_name_results: list = []
sales_price_results: list = []
main_screen = None

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

'''
close_iframe
iframe offer appears after about 6 - 10 seconds
close_iframe switches to iframe closes and switches
back to parent frame to resume.
'''


def close_iframe(driver: webdriver.Firefox):
    # closes iframe pop up box
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, 'lightbox-iframe-9d8cb083-db92-488b-9101-eff3183f4a23'))
    )
    close_lightbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'button2'))
    )
    close_lightbox.click()

    driver.switch_to.parent_frame()


def redbubble_search(driver: webdriver.Firefox, key_phrase: str):

    url: str = 'https://www.redbubble.com'

    driver.get(url)

    search_query = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'query'))
    )
    search_query.click()
    search_query.send_keys(key_phrase)

    search_query.send_keys(Keys.ENTER)

    title_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'SearchResults'))
    )
    results.append(title_text.text)

    close_iframe(driver)

    grid_of_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'SearchResultsGrid'))
    )

    '''
    Design Title pull
    pulls all design titles
    appends to array -> shirt_title_results
    
    '''
    shirt_titles = grid_of_results.find_elements(
        By.XPATH, '//a/div/div[3]/div/div[1]/span')

    # shirt_titles = grid_of_results.find_elements(By.CSS_SELECTOR, 'span')

    for shirt_title in shirt_titles:
        shirt_title_results.append(shirt_title.text)

    '''
    Artists names
    pulls artists names to be collected in
    -> artist_name_results array
    replaces string 'by ' and strips() whitespace
    from name prior to appending data.
    '''
    artist_names = grid_of_results.find_elements(
        By.XPATH, '//a/div/div[3]/div/div[1]/div/span')

    for artist_name in artist_names:
        name = artist_name.text
        fix_name = name.replace('By ', '').strip()
        artist_name_results.append(fix_name)

    sleep(3)

    driver.quit()


redbubble_search(driver=driver, key_phrase='robot art')


sleep(1)
print('---------------')
print('my findings are.')
for finds in results:
    print(finds)
    print(shirt_title_results)
    print(artist_name_results)
