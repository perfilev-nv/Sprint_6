import pytest
from data import base_url
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()