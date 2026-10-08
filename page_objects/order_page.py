from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    # Шаг 1 — «Для кого самокат»
    NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION_INPUT = By.XPATH, '//input[@placeholder="* Станция метро"]'
    METRO_STATION_SELECTED = By.XPATH, '//li[contains(@class, "select-search__option") and contains(@class, "selected")]'
    PHONE_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'

    # Шаг 2 — «Про аренду»
    WHEN_INPUT = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_DROPDOWN = By.CLASS_NAME, "Dropdown-placeholder"
    RENTAL_PERIOD_TWO_DAYS = By.XPATH, '//div[@class="Dropdown-menu"]//div[text()="двое суток"]'
    COMMENT_INPUT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    ORDER_CONFIRM_BUTTON = By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]'
    YES_BUTTON = By.XPATH, '//button[text()="Да"]'
    SUCCESS_MODAL = By.XPATH, '//div[contains(@class, "Order_Modal__")]//div[contains(@class, "Order_ModalHeader__")]'

    def fill_first_step(self, name, surname, address, metro_index, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click(self.METRO_STATION_INPUT)
        opts = self.find_elements((By.XPATH, '//button[contains(@class, "select-search__option")]'))
        option_element = opts[metro_index]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", option_element
        )
        option_element.click()
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    def fill_second_step(self, delivery_date, comment):
        self.send_keys(self.WHEN_INPUT, delivery_date)
        self.send_keys(self.WHEN_INPUT, "\ue007")
        self.click(self.RENTAL_PERIOD_DROPDOWN)
        self.click(self.RENTAL_PERIOD_TWO_DAYS)
        self.send_keys(self.COMMENT_INPUT, comment)
        self.click(self.ORDER_CONFIRM_BUTTON)
        self.click(self.YES_BUTTON)

    def get_success_message(self):
        return self.wait_for_visibility(self.SUCCESS_MODAL).text