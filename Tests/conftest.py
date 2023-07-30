import logging

import pytest

from Config import config_data
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

log = logging.getLogger(__name__)


def pytest_configure(config):
    """Create log file if log file is not mentioned in ini file"""
    if not config.option.log_file:
        config.option.log_file = '../execution.log'


def initiate_chromedriver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()


def initiate_firefoxdriver(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()


def initiate_iedriver(request):
    driver = webdriver.Ie(IEDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()


def initiate_edgedriver(request):
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()


@pytest.fixture(params=[config_data.browser], autouse=True, scope=config_data.driver_scope)
def init_driver(request):
    if request.param == "chrome":
        if not config_data.debug:
            logging.info("\n\n=====starting test(" + request.node.name + ")================")
            yield from initiate_chromedriver(request)
