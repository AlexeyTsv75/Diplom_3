from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    @allure.step('Инициируем дайвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Ждем видимость элемента')
    def wait_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ждем кликабельности элемента')
    def wait_clickable_of_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ждем текст в элементе')
    def wait_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Ждем отсутствия текста в элементе')
    def wait_text_not_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Ждем присутствия элемента')
    def wait_presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Находим элемент с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

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

    @allure.step('Перемещаем элемент')
    def move_element_to_target(self, driver, locator_source, locator_target):
        element = self.find_element_with_wait(locator_source)
        target = self.find_element_with_wait(locator_target)
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target).perform()
