from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.click()

    def send_keys(self, locator, value, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
        element.send_keys(value)

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def go_to_last_tab(self, timeout=10):
        handles = WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_contains(self, substring, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: substring in d.current_url
        )