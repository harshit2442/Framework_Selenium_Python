import logging
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from KeywordLibrary.keyword import GenericMethods


class GooglePage(GenericMethods):
    """======================Locator=============================="""

    search_textbox = (By.NAME, "q")
    search_button = (By.NAME, "btnk")
    google_cookies_popup = (By.XPATH, "//+[text()='Accept all']")

    """=====================Constructor==========================="""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """=====================Page Functions========================"""
    @allure.step("Navigate to page")
    def navigate_to_page(self, url):
        self.navigate(url)
        if self.is_element_present(self.google_cookies_popup):
            self.click_on_element(self.google_cookies_popup)
        logging.info("Navigated successfully to : %s" % url)
        self.take_screenshot()

    @allure.step("Type text")
    def type_text_in_search_box(self, value):
        search_box = self.find_element(self.search_textbox)
        search_box.send_keys(value)
        search_box.send_keys(Keys.ENTER)
        actual_title = self.get_title()
        time.sleep(2)
        assert actual_title == "India - Google Search"
        logging.info("Title matched")
        self.take_screenshot()
