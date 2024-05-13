import allure
import data
import helper
from locators.order_lent_locator import OrderLentLocator
from pages.profile_page import ProfilePage


class OrderLentPage(ProfilePage):
    @allure.step('Открываем окно заказа кликом по кнопке заказа')
    def open_order_window_by_click_order(self):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        self.click_on_element(OrderLentLocator.LENT_FIRST_ORDER)
        element = self.find_elements(OrderLentLocator.ORDER_DESCRIPTION_WINDOW)
        return len(element)

    @allure.step('Сравниваем заказ из истории заказа с заказами в ленте заказа')
    def check_order_from_order_history_is_in_order_lent(self, token, order_number):
        self.wait_visibility_of_element_located(OrderLentLocator.ORDERS)
        elements = self.find_elements(OrderLentLocator.ORDERS)
        i = 0
        for element in elements:
            text = element.text
            if order_number in text:
                i = i+1
        helper.delete_user(token)
        return i

    @allure.step('Получаем значение счетчика всех заказов')
    def get_counter_all_oder(self):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        counter = self.get_text_from_element(OrderLentLocator.ALL_ORDER)
        return counter

    @allure.step('Получаем значение счетчика сегодняшних заказов')
    def get_counter_today_oder(self):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        counter = self.get_text_from_element(OrderLentLocator.TODAY_ORDER)
        return counter

    @allure.step('Сравниваем номер сделанного заказа с заказами в разделе В работе ')
    def check_made_order_number_is_in_work(self, order_number, token):
        self.wait_text_to_be_present_in_element(OrderLentLocator.ORDERS_IN_WORK, 'Все текущие заказы готовы!')
        self.wait_text_not_to_be_present_in_element(OrderLentLocator.ORDERS_IN_WORK, 'Все текущие заказы готовы!')
        self.wait_presence_of_element_located(OrderLentLocator.ORDERS_IN_WORK)
        elements = self.find_elements(OrderLentLocator.ORDERS_IN_WORK)
        i = 0
        for element in elements:
            text = element.text
            if order_number in text:
                i = i + 1
        helper.delete_user(token)
        return i
