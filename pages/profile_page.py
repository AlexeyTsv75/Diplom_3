import data
import helper
from locators.login_locator import LoginLocator
from locators.main_page_locator import MainPageLocator
from locators.profile_locator import ProfileLocator
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class ProfilePage(BasePage):

    @allure.step('Входим в личный кабинет нажимая кнопку Личного кабинета')
    def enter_profile_by_click_profile_button(self):
        token = self.login_created_user()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocator.MAKE_ORDER_BUTTON))

        self.get_url(data.URL_MAIN_PAGE)
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(MainPageLocator.PROFILE_BUTTON))
        self.click_on_element_without_wait(MainPageLocator.PROFILE_BUTTON)
        result = self.get_text_from_element(ProfileLocator.EXIT_PROFILE_BUTTON)
        helper.delete_user(token)
        return result

    @allure.step('Входим в Историю заказов нажимая кнопку История заказов')
    def enter_order_history_by_click_history_button(self):
        token = self.login_created_user()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocator.MAKE_ORDER_BUTTON))
        self.get_url(data.URL_MAIN_PAGE)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(MainPageLocator.PROFILE_BUTTON))
        self.click_on_element_without_wait(MainPageLocator.PROFILE_BUTTON)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ProfileLocator.ORDER_HISTORY))
        self.click_on_element_without_wait(ProfileLocator.ORDER_HISTORY)
        result = self.find_element_with_wait(ProfileLocator.ORDER_HISTORY)
        helper.delete_user(token)
        return result

    @allure.step('Выходим из Личного кабинета нажимая кнопку Выход')
    def exit_profile_by_click_exit_button(self):
        token = self.login_created_user()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocator.MAKE_ORDER_BUTTON))
        self.get_url(data.URL_MAIN_PAGE)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(MainPageLocator.PROFILE_BUTTON))
        self.click_on_element_without_wait(MainPageLocator.PROFILE_BUTTON)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ProfileLocator.EXIT_PROFILE_BUTTON))
        self.click_on_element_without_wait(ProfileLocator.EXIT_PROFILE_BUTTON)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(LoginLocator.LOGIN_BUTTON))
        result = self.get_text_from_element(LoginLocator.HEADER_ENTER)
        helper.delete_user(token)
        return result
