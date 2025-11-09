import pytest
from selenium import webdriver
from url import SCOOTER_ORDER_URL

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(SCOOTER_ORDER_URL)
    yield browser
    browser.quit()