from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def wait_visibility(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, time=3):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
        return self.wait_visibility(locator).text

    def send_keys(self, locator, text):
        self.wait_visibility(locator).send_keys(text)

    def scroll_to_element(self, locator, time=3):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)