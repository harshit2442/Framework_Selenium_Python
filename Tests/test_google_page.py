import allure
import pytest
from Pages.GoogleHome_Page import GooglePage
from Tests.test_base import BaseTest


class TestGoogleSearch(BaseTest):
    @allure.title("Search text in Google Page")
    def test_search_google(self):
        self.search_page = GooglePage(self.driver)
        self.search_page.navigate_to_page(url="https://www.google.com/")
        self.search_page.type_text_in_search_box(value="India")
