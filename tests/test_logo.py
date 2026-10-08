from page_objects.main_page import MainPage


class TestLogos:
    def test_scooter_logo_leads_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_logo_scooter()
        assert main_page.driver.current_url == MainPage.URL

    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_logo_yandex()
        main_page.go_to_last_tab()
        main_page.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in main_page.driver.current_url