from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    def fill_customer_page(self, first_name, last_name, address, metro_station, phone):

        self.find_element(OrderPageLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(OrderPageLocators.LAST_NAME).send_keys(last_name)
        self.find_element(OrderPageLocators.ADDRESS).send_keys(address)
        self.find_element(OrderPageLocators.METRO_STATION_FIELD).click()
        station_option_locator = (By.XPATH, OrderPageLocators.METRO_STATION[1].format(metro_station))
        self.find_element(station_option_locator).click()
        self.find_element(OrderPageLocators.PHONE).send_keys(phone)

        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_rental_page(self, date, rent_time):

        self.find_element(OrderPageLocators.DATE).send_keys(date)
        self.find_element(OrderPageLocators.DATE).send_keys(Keys.RETURN)
        self.click_element(OrderPageLocators.RENT_TIME_FIELD)
        rent_time_option_locator = (By.XPATH, OrderPageLocators.RENT_TIME_OPTION[1].format(rent_time))
        self.click_element(rent_time_option_locator)

        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.find_element(OrderPageLocators.CONFIRM_BUTTON).click()

    def get_success_order_text_element(self):
        return self.find_element(OrderPageLocators.SUCCESS_ORDER_TEXT)
