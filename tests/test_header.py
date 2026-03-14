import allure
from data import base_url
from pages.main_page import MainPage

@allure.parent_suite("Sprint 6")
@allure.suite("Header")
@allure.sub_suite('Логотипы')
@allure.feature("Header")
class TestHeader:

    @allure.title("Открытие главной страницы при нажатии на логотип 'Самоката'")
    def test_open_main_page_via_scooter_logo(self,driver):
        main_page = MainPage(driver)

        with allure.step("Принять cookies"):
            main_page.accept_cookies()

        with allure.step("Открыть страницу заказа"):
            main_page.click_order_top()

        with allure.step('Нажать логотип "Самоката"'):
            main_page.click_scooter_logo()

        with allure.step("Проверить что открылась главная страница"):
            assert main_page.get_current_url() == base_url


    @allure.title("Открытие главной страницы Дзена при нажатии на логотип Яндекса")
    def test_open_dzen_page_via_yandex_logo(self, driver):
        main_page = MainPage(driver)

        with allure.step("Принять cookies"):
            main_page.accept_cookies()

        original_window = main_page.current_window_handle()

        with allure.step('Нажать логотип Яндекса'):
            main_page.open_dzen_via_yandex_logo(original_window)

        with allure.step('Проверить что открылась главная страница Дзена'):
            assert "dzen.ru" in main_page.get_current_url()