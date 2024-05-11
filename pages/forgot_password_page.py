import data
from pages.base_page import BasePage
from locators.forgot_password_locator import ForgotPasswordLocator
from selenium.webdriver.support.wait import WebDriverWait
import allure


class ForgotPasswordPage(BasePage):
    @allure.step('Переход на страницу восстановления пароля кликая на кнопку восстановить пароль')
    def move_to_forgot_password_page_by_click_password_recovery_button(self):
        self.get_url(data.URL_MAIN_PAGE+data.URL_LOGIN)
        self.click_on_element(ForgotPasswordLocator.PASSWORD_RECOVER_BUTTON)
        return self.get_text_from_element(ForgotPasswordLocator.PASSWORD_RECOVER_HEADER)

    @allure.step('Вводим емейл для восстановления пароля')
    def input_email_and_click_restore_button_for_password_recovery(self):
        self.get_url(data.URL_MAIN_PAGE+data.URL_PASSWORD_RECOVERY)
        self.click_on_element(ForgotPasswordLocator.EMAIL_PLACEHOLDER)
        self.set_text_to_element(ForgotPasswordLocator.EMAIL_INPUT, "alex2024@ya.ru")
        self.click_on_element(ForgotPasswordLocator.RECOVERY_BUTTON)
        return self.get_text_from_element(ForgotPasswordLocator.INPUT_CODE)

    @allure.step('Кликаем по кнопке показать/скрыть пароль')
    def password_field_activated_by_click_eye_button(self):
        self.get_url(data.URL_MAIN_PAGE + data.URL_PASSWORD_RECOVERY)
        self.click_on_element(ForgotPasswordLocator.EMAIL_PLACEHOLDER)
        self.set_text_to_element(ForgotPasswordLocator.EMAIL_INPUT, "alex2024@ya.ru")
        self.click_on_element(ForgotPasswordLocator.RECOVERY_BUTTON)
        WebDriverWait(self.driver, 5)
        self.click_on_element(ForgotPasswordLocator.PASSWORD_FIELD)
        self.set_text_to_element(ForgotPasswordLocator.PASSWORD_INPUT, "2345678")
        self.click_on_element(ForgotPasswordLocator.EYE_SIGN_HIDE)
        return self.find_element_with_wait(ForgotPasswordLocator.PASSWORD_INPUT).get_attribute('type')
