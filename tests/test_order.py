import allure
import pytest
from data import order_data
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.parent_suite("Sprint 6")
@allure.suite("Заказ самоката")
@allure.sub_suite("Позитивный сценарий заказа")
@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката кнопкой вверху страницы")
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone, date, rent_time", order_data)
    def test_order_positive_flow_via_top_button(self, driver, first_name,
                                 last_name, address, metro_station,
                                 phone, date, rent_time):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Принять cookies"):
            main_page.accept_cookies()

        with allure.step("Нажать кнопку заказа вверху страницы"):
            main_page.click_order_top()

        with allure.step("Заполнить форму пользователя"):
            order_page.fill_customer_page(first_name, last_name, address, metro_station, phone)

        with allure.step("Заполнить данные аренды"):
            order_page.fill_rental_page(date, rent_time)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить отображение текста успешного заказа"):
            element = order_page.get_success_order_text_element()

        assert element.is_displayed()

    @allure.title("Позитивный сценарий заказа самоката кнопкой внизу")
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone, date, rent_time", order_data)
    def test_order_positive_flow_via_bottom_button(self, driver, first_name,
                                 last_name, address, metro_station,
                                 phone, date, rent_time):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Принять cookies"):
            main_page.accept_cookies()

        with allure.step("Нажать кнопку заказа внизу страницы"):
            main_page.click_order_bottom()

        with allure.step("Заполнить форму пользователя"):
            order_page.fill_customer_page(first_name, last_name, address, metro_station, phone)

        with allure.step("Заполнить данные аренды"):
            order_page.fill_rental_page(date, rent_time)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить отображение текста успешного заказа"):
            element = order_page.get_success_order_text_element()

        assert element.is_displayed()