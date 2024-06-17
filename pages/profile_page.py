import helper
from locators.login_locator import LoginLocator
from locators.profile_locator import ProfileLocator
import allure
from pages.main_page import MainPage


class ProfilePage(MainPage):

    @allure.step('Проверяем вход в личный кабинет')
    def check_enter_profile_by_click_profile_button(self, token):
        result = self.get_text_from_element(ProfileLocator.EXIT_PROFILE_BUTTON)
        helper.delete_user(token)
        return result

    @allure.step('Входим в Историю заказов нажимая кнопку История заказов')
    def enter_order_history_by_click_history_button(self, token):
        self.wait_clickable_of_element(ProfileLocator.ORDER_HISTORY)
        self.click_on_element_without_wait(ProfileLocator.ORDER_HISTORY)
        result = self.find_element_with_wait(ProfileLocator.ORDER_HISTORY)
        helper.delete_user(token)
        return result

    @allure.step('Берем номер заказа из истории заказщв')
    def get_number_of_order_from_order_history(self):
        self.click_on_element(ProfileLocator.ORDER_HISTORY)
        order_number = self.get_text_from_element(ProfileLocator.LAST_ORDER)
        return order_number

    @allure.step('Выходим из Личного кабинета нажимая кнопку Выход')
    def exit_profile_by_click_exit_button(self, token):
        self.wait_clickable_of_element(ProfileLocator.EXIT_PROFILE_BUTTON)
        self.click_on_element_without_wait(ProfileLocator.EXIT_PROFILE_BUTTON)
        self.wait_clickable_of_element(LoginLocator.LOGIN_BUTTON)
        result = self.get_text_from_element(LoginLocator.HEADER_ENTER)
        helper.delete_user(token)
        return result
