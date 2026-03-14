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

    def switch_to_opened_browser_window(self, original_window, windows_amount, time=3):
        WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(windows_amount))

        new_window = None
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                new_window = window_handle
                self.driver.switch_to.window(window_handle)
                break

    def wait_for_opening_url_with_specific_string(self, specific_string, time=3):
        return WebDriverWait(self.driver, time).until(EC.url_contains(specific_string))

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def current_window_handle(self):
        return self.driver.current_window_handle