import helper
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
        token = order_lent_page.make_order_login_user(driver)
        order_lent_page.move_to_profile_by_click_profile_button()
        order_number = order_lent_page.get_number_of_order_from_order_history()
        order_lent_page.move_to_order_lent_by_click_order_lent_button()
        result = order_lent_page.check_order_from_order_history_is_in_order_lent(token, order_number)
        assert result == 1

    @allure.title('Проверяем увеличение Счетчика всех заказов при создании нового заказа')
    def test_increase_counter_all_oder_create_new_order_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        prev_result = order_lent_page.get_counter_all_oder()
        token = order_lent_page.make_order_login_user(driver)
        result = order_lent_page.get_counter_all_oder()
        helper.delete_user(token)
        assert int(result)-int(prev_result) > 0

    @allure.title('Проверяем увеличение Счетчика сегодняшних заказов при создании нового заказа')
    def test_increase_counter_today_oder_create_new_order_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        prev_result = order_lent_page.get_counter_today_oder()
        token = order_lent_page.make_order_login_user(driver)
        result = order_lent_page.get_counter_today_oder()
        helper.delete_user(token)
        assert int(result) - int(prev_result) > 0

    @allure.title('Проверяем, что номер сделанного заказа появляется в разделе В работе')
    def test_made_order_number_is_in_work_success(self, driver):
        order_lent_page = OrderLentPage(driver)
        token = order_lent_page.make_order_login_user(driver)
        order_lent_page.move_to_profile_by_click_profile_button()
        order_number = order_lent_page.get_number_of_order_from_order_history()
        order_number = order_number.replace('#', '')
        order_lent_page.move_to_order_lent_by_click_order_lent_button()
        result = order_lent_page.check_made_order_number_is_in_work(order_number, token)
        assert result == 1
