from selenium import webdriver


class Browser:
    '''
    class Browser
    parameter: driver
    '''

    def __init__(self, driver):
        self.driver = driver

    def browser(self):
        '''
        function: browser
        params: 
            self
        returns: 
            self.driver object

        description: opens chrome browser and returns
            self.driver object
            to be called when needed.
        '''
        self.driver = webdriver.Chrome()
        return self.driver

    def close_browser(self):
        '''
        function: close_browser
        params: self

        returns: None

        description: 
            closes chrome browser
            quits chrome browser         
        '''

        self.driver.close()
        self.driver.quit()
