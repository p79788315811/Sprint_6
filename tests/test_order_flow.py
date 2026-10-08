import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


class TestOrderFlow:
    @pytest.mark.parametrize(
        "entry_point_order",
        [
            {"func": "click_order_button_top"},
            {"func": "click_order_button_bottom"},
        ],
    )
    @pytest.mark.parametrize(
        "first_step, second_step",
        [
            (
                {
                    "name": "Иван",
                    "surname": "Петров",
                    "address": "Москва, ул. Ленина, 1",
                    "metro_index": 1,
                    "phone": "+79161234567",
                },
                {
                    "delivery_date": "2026-10-12",
                    "comment": "Позвонить за час",
                },
            ),
            (
                {
                    "name": "Анна",
                    "surname": "Смирнова",
                    "address": "Москва, Ленинградский проспект, 10",
                    "metro_index": 3,
                    "phone": "+79998887766",
                },
                {
                    "delivery_date": "2026-10-15",
                    "comment": "Доставка после 18:00",
                },
            ),
        ],
    )
    def test_create_order(self, driver, entry_point_order, first_step, second_step):
        main_page = MainPage(driver)
        main_page.open()
        getattr(main_page, entry_point_order["func"])()

        order_page = OrderPage(driver)
        order_page.fill_first_step(**first_step)
        order_page.fill_second_step(**second_step)

        message = order_page.get_success_message()
        assert "Заказ оформлен" in message