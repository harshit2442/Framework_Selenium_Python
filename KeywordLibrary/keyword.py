"""
This Page contains all generic methods that will be used in automating a page
"""
import logging

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config import config_data


class GenericMethods:
    template = "An exception of type {0} occurred. Arguments: \n{1!r}"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Generic function
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self):
        get_title = self.driver.title
        return get_title

    def enter_text_and_enter(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        self.driver.send_keys(Keys.ENTER)

    def navigate(self, url):
        try:
            self.driver.get(url)
            logging.info("--------Navigated to : " + url)
        except Exception as err:
            logging.error("-------unable to navigate to : " + url)
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)

    def is_element_present(self, locator):
        try:
            element = WebDriverWait(self.driver, config_data.globalWaitTime).until(
                EC.visibility_of_element_located(locator))
            logging.info("---------Element is present: " + str(locator[0]) + str(locator[1]))
            return bool(element)
        except:
            logging.error("---------Element is not present: " + str(locator[0]) + str(locator[1]))

    def take_screenshot(self):
        try:
            if config_data.enableScreeshot == "true":
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot',
                              attachment_type=AttachmentType.PNG)
                logging.info("Screenshot taken")
        except Exception as err:
            logging.error("Unable to take screenshot")
            message = self.template.format(type(err).__name__, err.args)
            raise type(err)(message)
