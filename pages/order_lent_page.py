import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import helper
from locators.main_page_locator import MainPageLocator
from locators.order_lent_locator import OrderLentLocator
from locators.profile_locator import ProfileLocator
from pages.base_page import BasePage


class OrderLentPage(BasePage):
    @allure.step('Открываем окно заказа кликом по кнопке заказа')
    def open_order_window_by_click_order(self):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        self.click_on_element(OrderLentLocator.LENT_FIRST_ORDER)
        element = self.find_elements_with_wait(OrderLentLocator.ORDER_DESCRIPTION_WINDOW)
        return len(element)

    @allure.step('Заказ из истории заказа есть в ленте заказа')
    def order_from_order_history_is_in_order_lent(self, driver):
        token = self.make_order_login_user(driver)
        self.click_on_element(MainPageLocator.PROFILE_BUTTON)
        self.click_on_element(ProfileLocator.ORDER_HISTORY)
        order_number = self.get_text_from_element(ProfileLocator.LAST_ORDER)
        self.click_on_element(MainPageLocator.ORDER_LENT_BUTTON)
        elements = self.find_elements_with_wait(OrderLentLocator.ORDERS)
        i = 0
        for element in elements:
            text = element.text
            if order_number in text:
                i = i+1
        helper.delete_user(token)
        return i

    @allure.step('Увеличиваем счетчик всех заказов создавая новый заказ')
    def increase_counter_all_oder_create_new_order(self, driver):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        prev_counter = self.get_text_from_element(OrderLentLocator.ALL_ORDER)
        token = self.make_order_login_user(driver)
        self.click_on_element(MainPageLocator.ORDER_LENT_BUTTON)
        counter = self.get_text_from_element(OrderLentLocator.ALL_ORDER)
        helper.delete_user(token)
        return int(counter) - int(prev_counter)

    @allure.step('Увеличиваем счетчик сегодняшних заказов создавая новый заказ')
    def increase_counter_today_oder_create_new_order(self, driver):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        prev_counter = self.get_text_from_element(OrderLentLocator.TODAY_ORDER)
        token = self.make_order_login_user(driver)
        self.click_on_element(MainPageLocator.ORDER_LENT_BUTTON)
        counter = self.get_text_from_element(OrderLentLocator.TODAY_ORDER)
        helper.delete_user(token)
        return int(counter) - int(prev_counter)

    @allure.step('Номер сделанного заказа появляется в разделе В работе ')
    def made_order_number_is_in_work(self, driver):
        token = self.make_order_login_user(driver)
        self.click_on_element(MainPageLocator.PROFILE_BUTTON)
        self.click_on_element(ProfileLocator.ORDER_HISTORY)
        order_number = self.get_text_from_element(ProfileLocator.LAST_ORDER)
        order_number = order_number.replace('#', '')
        self.click_on_element(MainPageLocator.ORDER_LENT_BUTTON)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(OrderLentLocator.ORDERS_IN_WORK, 'Все текущие заказы готовы!'))
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.text_to_be_present_in_element(OrderLentLocator.ORDERS_IN_WORK, 'Все текущие заказы готовы!'))
        elements = self.find_elements_with_wait(OrderLentLocator.ORDERS_IN_WORK)
        i = 0
        for element in elements:
            text = element.text
            if order_number in text:
                i = i + 1
        helper.delete_user(token)
        return i




