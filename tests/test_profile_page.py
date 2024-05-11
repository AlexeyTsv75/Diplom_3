from pages.profile_page import ProfilePage
import allure


class TestProfilePage:
    @allure.title('Проверяем вход в Личный кабинет нажатием кнопки Личный кабинет')
    def test_enter_profile_by_click_profile_button_success(self, driver):
        profile_page = ProfilePage(driver)
        assert profile_page.enter_profile_by_click_profile_button() == "Выход"

    @allure.title('Проверяем вход в Историю заказов нажимая кнопку История заказов')
    def test_enter_order_history_by_click_history_button_success(self, driver):
        profile_page = ProfilePage(driver)
        result = profile_page.enter_order_history_by_click_history_button()
        assert 'Account_link_active' in result.get_attribute('class')

    @allure.title('Проверяем выход из Личного кабинета нажимая кнопку Выход')
    def test_exit_profile_by_click_exit_button_success(self, driver):
        profile_page = ProfilePage(driver)
        result = profile_page.exit_profile_by_click_exit_button()
        assert result == 'Вход'
