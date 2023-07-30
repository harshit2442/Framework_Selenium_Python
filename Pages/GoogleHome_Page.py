import logging

from selenium.webdriver.common.by import By

from KeywordLibrary.keyword import GenericMethods


class GooglePage(GenericMethods):
    """======================Locator=============================="""

    search_textbox = (By.NAME, "q")
    search_button = (By.NAME, "btnk")
    google_cookies_popup = (By.XPATH, "//+[text()='Accept all']")

    def __init__(self, driver):
        super().__init__(driver)

    """=====================Page Functions========================"""

    def navigate_to_page(self, url):
        self.navigate(url)
        if self.is_element_present(self.google_cookies_popup):
            self.click_on_element(self.google_cookies_popup)
        logging.info("Navigated successfully to : %s" % url)

    def type_text_in_search_box(self, value):
        self.enter_text_and_enter(self.search_textbox, value)
        actual_title = self.get_title()
        assert actual_title == "Google"
