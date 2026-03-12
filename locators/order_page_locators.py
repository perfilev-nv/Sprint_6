from selenium.webdriver.common.by import By

class OrderPageLocators:

    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//li[@class='select-search__row']/button/div[text()='{}']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_FIELD = (By.XPATH, "//div[@class='Dropdown-control']")
    RENT_TIME_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")

    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_ORDER_TEXT = (By.XPATH, "//div[text()='Заказ оформлен']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

