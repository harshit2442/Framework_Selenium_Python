"""
This Page contains all generic methods that will be used in automating a page
"""

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GenericMethods:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))





