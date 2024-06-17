from pages.main_page import MainPage
import allure


class TestMainPage:
    @allure.title('Проверяем переход в Конструктор нажатием кнопки Конструктор')
    def test_move_to_constructor_by_click_constructor_button_success(self, driver):
        main_page = MainPage(driver)
        result = main_page.move_to_constructor_by_click_constructor_button()
        assert result == 'Соберите бургер'

    @allure.title('Проверяем переход в Ленту заказов нажатием кнопки Лента заказов')
    def test_move_to_order_lent_by_click_order_lent_button_success(self, driver):
        main_page = MainPage(driver)
        result = main_page.move_to_order_lent_by_click_order_lent_button()
        assert result == 'Лента заказов'

    @allure.title('Проверяем открытие окна ингредиента кликом по ингредиенту')
    def test_open_ingredient_window_by_click_ingredient_success(self, driver):
        main_page = MainPage(driver)
        result = main_page.open_ingredient_window_by_click_ingredient()
        assert result == 'Детали ингредиента'

    @allure.title('Проверяем закрытие окна ингредиента кликом по Х')
    def test_close_ingredient_window_by_click_x_success(self, driver):
        main_page = MainPage(driver)
        result = main_page.close_ingredient_window_by_click_x()
        assert result == 'Начинки'

    @allure.title('Проверяем увеличение счетчика перемещая ингредиент в заказ')
    def test_increase_counter_by_move_ingredient_to_order_success(self, driver):
        main_page = MainPage(driver)
        result = main_page.increase_counter_by_move_ingredient_to_order(driver)
        assert result > 0

    @allure.title('Проверяем успешное создание заказа залогиненым пользователем')
    def test_make_order_by_login_user_success(self, driver):
        main_page = MainPage(driver)
        result = main_page.make_order_by_login_user(driver)
        assert result == 'Ваш заказ начали готовить'
