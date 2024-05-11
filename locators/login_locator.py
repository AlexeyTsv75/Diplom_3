from selenium.webdriver.common.by import By


class LoginLocator:
    LOGIN_E_MAIL = By.XPATH, ".//input[@name='name']"
    LOGIN_PASSWORD = By.XPATH, ".//input[@name='Пароль']"
    LOGIN_BUTTON = By.XPATH, ".//button[text() = 'Войти']"
    HEADER_ENTER = By.XPATH, ".//h2[text() = 'Вход']"
