import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1400")
    options.add_argument("--height=900")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()