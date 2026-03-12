import allure
import pytest
from data import order_data, base_url
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.parent_suite("Sprint 6")
@allure.suite("Заказ самоката")
@allure.sub_suite("Позитивный сценарий заказа")
@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone, date, rent_time", order_data)
    @pytest.mark.parametrize("button", ["top", "bottom"])
    def test_order_positive_flow(self, driver, first_name,
                                 last_name, address, metro_station,
                                 phone, date, rent_time, button):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Принять cookies"):
            main_page.accept_cookies()

        match button:
            case "top":
                main_page.click_order_top()
            case "bottom":
                main_page.click_order_bottom()

        with allure.step("Заполнить форму пользователя"):
            order_page.fill_customer_page(first_name, last_name, address, metro_station, phone)

        with allure.step("Заполнить данные аренды"):
            order_page.fill_rental_page(date, rent_time)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление заказа"):
            success_text = order_page.get_success_order_text()

        assert "Заказ оформлен" in success_text

        order_page.click_order_status_button()

        with allure.step('Нажать логотип "Самоката"'):
            main_page.click_scooter_logo()

        with allure.step("Проверить что открылась главная страница"):
            assert driver.current_url == base_url

        original_window = driver.current_window_handle

        with allure.step('Нажать логотип Яндекса'):
            main_page.open_dzen_via_yandex_logo(original_window)

        with allure.step('Проверить что открылась главная страница Дзена'):
            assert "dzen.ru" in driver.current_url

        driver.close()
        driver.switch_to.window(original_window)

