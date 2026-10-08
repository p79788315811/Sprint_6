from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    # Cookie-баннер
    COOKIE_BANNER = By.ID, "rcc-confirm-button"

    # Логотипы
    LOGO_SCOOTER = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"

    # Кнопки заказа
    ORDER_BUTTON_TOP = By.CLASS_NAME, "Button_Button__ra12g"
    ORDER_BUTTON_BOTTOM = By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM")]'

    # Блок «Вопросы о важном»
    QUESTION_LOCATOR = (By.XPATH, '//div[@id="accordion__heading-{index}"]')
    ANSWER_LOCATOR = (By.XPATH, '//div[@id="accordion__panel-{index}"]/p')

    def open(self):
        self.driver.get(self.URL)
        self.close_cookie_banner_if_present()

    def close_cookie_banner_if_present(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.COOKIE_BANNER)
            ).click()
        except Exception:
            pass

    def click_order_button_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        element = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.click(self.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)

    # Вопросы о важном
    def click_question(self, index):
        locator = (By.XPATH, self.QUESTION_LOCATOR[1].format(index=index))
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return self.click(locator)

    def get_answer_text(self, index):
        locator = (By.XPATH, self.ANSWER_LOCATOR[1].format(index=index))
        return self.wait_for_visibility(locator).text