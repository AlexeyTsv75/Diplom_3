from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
import data
import helper
from locators.login_locator import LoginLocator
from locators.main_page_locator import MainPageLocator
from locators.order_lent_locator import OrderLentLocator


class BasePage:

    @allure.step('Инициируем дайвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Находим элемент с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Находим элементы с ожиданием')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Находим элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Находим элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Кликаем по элементу с ожиданием')
    def click_on_element_without_wait(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Кликаем по элементам')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        element_text = element.text
        return element_text

    @allure.step('Передаем текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Регистрируем созданного пользователя')
    def login_created_user(self):
        user = helper.new_user_creation()
        self.get_url(data.URL_MAIN_PAGE+data.URL_LOGIN)
        self.set_text_to_element(LoginLocator.LOGIN_E_MAIL, user['email'])
        self.set_text_to_element(LoginLocator.LOGIN_PASSWORD, user['password'])
        self.click_on_element(LoginLocator.LOGIN_BUTTON)
        return user['token']

    @allure.step('Перемещаем элемент')
    def move_element_to_target(self, driver, locator_source, locator_target):
        element = self.find_element_with_wait(locator_source)
        target = self.find_element_with_wait(locator_target)
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Делаем заказ зарегистрированного пользователя')
    def make_order_login_user(self, driver):
        token = self.login_created_user()
        self.move_element_to_target(driver, MainPageLocator.FLU_BUN, MainPageLocator.MAKE_ORDER_BUTTON)
        self.click_on_element(MainPageLocator.MAKE_ORDER_BUTTON)
        WebDriverWait(self.driver, 10).until(
           expected_conditions.text_to_be_present_in_element(MainPageLocator.ORDER_NUMBER, '9999'))
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.text_to_be_present_in_element(MainPageLocator.ORDER_NUMBER, '9999'))
        self.click_on_element(OrderLentLocator.X_CLOSE)
        return token



