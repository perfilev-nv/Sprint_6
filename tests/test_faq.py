import allure
import pytest
from data import faq_answers
from pages.main_page import MainPage


@allure.parent_suite("Sprint 6")
@allure.suite("Главная страница")
@allure.sub_suite('Блок "Вопросы о важном"')
@allure.feature("Главная страница")
class TestFaq:

    @allure.title("Раскрытие вопроса №{index} в блоке 'Вопросы о важном'")
    @pytest.mark.parametrize("index, expected", faq_answers, ids=[f"FAQ {i}" for i in range(len(faq_answers))])
    def test_faq_question_answer(self, driver, index, expected):
        page = MainPage(driver)

        with allure.step("Принять cookies"):
            page.accept_cookies()

        with allure.step("Открыть вопрос"):
            page.click_faq_question(index)

        with allure.step("Проверить текст ответа"):
            answer = page.get_answer(index)

        assert answer == expected