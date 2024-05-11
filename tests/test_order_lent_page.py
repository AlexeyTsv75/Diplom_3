from pages.order_lent_page import OrderLentPage
import allure


class TestOrderLentPage:

    @allure.title('Проверяем открытие окна заказа кликая по заказу')
    def test_open_order_window_by_click_order_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        result = order_lent_page.open_order_window_by_click_order()
        assert result == 1

    @allure.title('Проверяем что заказ из Истории заказов есть в Ленте заказов')
    def test_order_from_order_history_is_in_order_lent_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        result = order_lent_page.order_from_order_history_is_in_order_lent(driver)
        assert result == 1

    @allure.title('Проверяем увеличение Счетчика всех заказов при создании нового заказа')
    def test_increase_counter_all_oder_create_new_order_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        result = order_lent_page.increase_counter_all_oder_create_new_order(driver)
        assert result > 0

    @allure.title('Проверяем увеличение Счетчика сегодняшних заказов при создании нового заказа')
    def test_increase_counter_today_oder_create_new_order_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        result = order_lent_page.increase_counter_today_oder_create_new_order(driver)
        assert result > 0

    @allure.title('Проверяем, что номер сделанного заказа появляется в разделе В работе')
    def test_made_order_number_is_in_work_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        result = order_lent_page.made_order_number_is_in_work(driver)
        assert result == 1
