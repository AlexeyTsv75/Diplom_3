import data
import helper
from locators.login_locator import LoginLocator
from locators.main_page_locator import MainPageLocator
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step('Переходим на страницу Конструктора, кликая кнопку Конструктор')
    def move_to_constructor_by_click_constructor_button(self):
        self.get_url(data.URL_MAIN_PAGE+data.ORDER_LENT)
        self.click_on_element(MainPageLocator.CONSTRUCTOR_BUTTON)
        result = self.get_text_from_element(MainPageLocator.SET_BURGER_HEADER)
        return result

    @allure.step('Переходим на Ленту заказов кликая по кнопке Лента заказов')
    def move_to_order_lent_by_click_order_lent_button(self):
        self.get_url(data.URL_MAIN_PAGE)
        self.click_on_element(MainPageLocator.ORDER_LENT_BUTTON)
        result = self.get_text_from_element(MainPageLocator.ORDER_LENT_HEADER)
        return result

    @allure.step('Открываем описание ингредиента кликая по ингредиенту')
    def open_ingredient_window_by_click_ingredient(self):
        self.get_url(data.URL_MAIN_PAGE)
        self.click_on_element(MainPageLocator.FLU_BUN)
        result = self.get_text_from_element(MainPageLocator.FLU_BUN_ING)
        return result

    @allure.step('Закрываем окно описания ингредиента кликая Х')
    def close_ingredient_window_by_click_x(self):
        self.get_url(data.URL_MAIN_PAGE)
        self.click_on_element(MainPageLocator.FLU_BUN)
        self.click_on_element(MainPageLocator.X_CLOSE_ING)
        result = self.get_text_from_element(MainPageLocator.FILLING_BUTTON)
        return result

    @allure.step('Увеличиваем счетчик перемещая ингредиент в заказ')
    def increase_counter_by_move_ingredient_to_order(self, driver):
        token = self.login_created_user()
        self.find_element_with_wait(MainPageLocator.MAKE_ORDER_BUTTON)
        prev_counter = self.get_text_from_element(MainPageLocator.FLU_BUN_COUNTER)
        self.move_element_to_target(driver, MainPageLocator.FLU_BUN, MainPageLocator.MAKE_ORDER_BUTTON)
        self.wait_text_to_be_present_in_element(MainPageLocator.FLU_BUN_COUNTER, '2')
        exist_counter = self.get_text_from_element(MainPageLocator.FLU_BUN_COUNTER)
        helper.delete_user(token)
        return int(exist_counter) - int(prev_counter)

    @allure.step('Делаем заказ для авторизованного пользователя')
    def make_order_by_login_user(self, driver):
        token = self.login_created_user()
        self.find_element_with_wait(MainPageLocator.MAKE_ORDER_BUTTON)
        self.move_element_to_target(driver, MainPageLocator.FLU_BUN, MainPageLocator.MAKE_ORDER_BUTTON)
        self.click_on_element(MainPageLocator.MAKE_ORDER_BUTTON)
        self.find_element_with_wait(MainPageLocator.YOUR_ORDER_IS_COCKING)
        result_1 = self.get_text_from_element(MainPageLocator.YOUR_ORDER_IS_COCKING)
        helper.delete_user(token)
        return result_1

    @allure.step('Регистрируем созданного пользователя')
    def login_created_user(self):
        user = helper.new_user_creation()
        self.get_url(data.URL_MAIN_PAGE+data.URL_LOGIN)
        self.set_text_to_element(LoginLocator.LOGIN_E_MAIL, user['email'])
        self.set_text_to_element(LoginLocator.LOGIN_PASSWORD, user['password'])
        self.click_on_element(LoginLocator.LOGIN_BUTTON)
        return user['token']

    @allure.step('Делаем заказ зарегистрированного пользователя')
    def make_order_login_user(self, driver):
        token = self.login_created_user()
        self.move_element_to_target(driver, MainPageLocator.FLU_BUN, MainPageLocator.MAKE_ORDER_BUTTON)
        self.click_on_element(MainPageLocator.MAKE_ORDER_BUTTON)
        self.wait_text_to_be_present_in_element(MainPageLocator.ORDER_NUMBER, '9999')
        self.wait_text_not_to_be_present_in_element(MainPageLocator.ORDER_NUMBER, '9999')
        self.click_on_element(MainPageLocator.X_CLOSE)
        return token

    @allure.step('Входим в личный кабинет нажимая кнопку Личного кабинета')
    def enter_profile_by_click_profile_button(self):
        token = self.login_created_user()
        self.wait_visibility_of_element_located(MainPageLocator.MAKE_ORDER_BUTTON)
        self.get_url(data.URL_MAIN_PAGE)
        self.wait_clickable_of_element(MainPageLocator.PROFILE_BUTTON)
        self.click_on_element_without_wait(MainPageLocator.PROFILE_BUTTON)
        return token

    @allure.step('Переходим в Ленту заказов кликая кнопку Лента заказов')
    def move_to_order_lent_by_click_order_lent_button(self):
        self.click_on_element(MainPageLocator.ORDER_LENT_BUTTON)

    @allure.step('Переходим в личный кабинет нажимая кнопку Личного кабинета')
    def move_to_profile_by_click_profile_button(self):
        self.wait_clickable_of_element(MainPageLocator.PROFILE_BUTTON)
        self.click_on_element_without_wait(MainPageLocator.PROFILE_BUTTON)
