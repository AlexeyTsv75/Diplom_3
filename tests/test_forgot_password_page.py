from pages.forgot_password_page import ForgotPasswordPage
import allure


class TestForgotPasswordPage:
    @allure.title('Проверяем переход на страницу восстановления пароля нажимая кнопку Восстановить пароль')
    def test_move_to_forgot_password_page_by_click_password_recovery_button_success(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        assert (forgot_password_page.move_to_forgot_password_page_by_click_password_recovery_button() ==
                'Восстановление пароля')

    @allure.title('Проверяем ввод емейл и нажатие кнопки восстановить для восстановления пароля')
    def test_input_email_and_click_restore_button_for_password_recovery_success(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        assert (forgot_password_page.input_email_and_click_restore_button_for_password_recovery() ==
                'Введите код из письма')

    @allure.title('Проверяем активацию поля ввода пароля нажатием иконы глаза')
    def test_password_field_activated_by_click_eye_button_success(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.password_field_activated_by_click_eye_button() == 'text'
