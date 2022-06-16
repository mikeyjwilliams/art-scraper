from time import sleep

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


from utils.utility import firefox_browser_open
from utils.utility import close_iframe
from pages.result import RedBubbleResultPage

# ENVIRONMENTAL VARIABLES
# from ENV import env

#   element = WebDriverWait(browser, 10).until(
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


'''
close_iframe
iframe offer appears after about 6 - 10 seconds
close_iframe switches to iframe closes and switches
back to parent frame to resume.
'''


browser = firefox_browser_open()


def redbubble_search(browser, key_phrase: str):

    search_query = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'query'))
    )
    search_query.click()
    search_query.send_keys(key_phrase)

    search_query.send_keys(Keys.ENTER)

    title_text = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'SearchResults'))
    )
    results.append(title_text.text)

    close_iframe(browser)

    grid_of_results = WebDriverWait(browser, 10).until(
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

    prices = grid_of_results.find_elements(
        By.XPATH, '//a[1]/div/div[3]/div/div[2]/div/div/span/span/span')

    for price in prices:
        sales_price_results.append(price.text)

    sleep(3)


redbubble_search(browser=browser, key_phrase='robot art')


sleep(1)
print('---------------')
print('my findings are.')
for finds in results:
    print(finds)
    print(shirt_title_results)
    print(artist_name_results)
    print(sales_price_results)
