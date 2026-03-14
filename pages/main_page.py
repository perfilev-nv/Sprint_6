from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass

    def click_faq_question(self, index):
        question_locator = (MainPageLocators.FAQ_QUESTIONS[0], MainPageLocators.FAQ_QUESTIONS[1].format(index))
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    def get_answer(self, index):
        answer_locator = (MainPageLocators.FAQ_ANSWERS[0], MainPageLocators.FAQ_ANSWERS[1].format(index))
        return self.get_text(answer_locator)

    def click_order_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def open_dzen_via_yandex_logo(self, original_window, time=3):
        self.click_element(MainPageLocators.YANDEX_LOGO)

        self.switch_to_opened_browser_window(original_window, 2)

        self.wait_for_opening_url_with_specific_string('dzen.ru')





