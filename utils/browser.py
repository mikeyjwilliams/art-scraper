from selenium import webdriver


def browser():

    driver = webdriver.Chrome()
    return driver


def close_browser(driver):

    driver.close()
    driver.quit()
