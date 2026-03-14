from selenium.webdriver.common.by import By

class MainPageLocators:

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    FAQ_QUESTIONS = (By.ID, "accordion__heading-{}")
    FAQ_ANSWERS = (By.ID, "accordion__panel-{}")

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home')]//button[text()='Заказать']")

    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

