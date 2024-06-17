from selenium.webdriver.common.by import By


class ForgotPasswordLocator:
    PASSWORD_RECOVER_BUTTON = By.XPATH, ".//a[text() = 'Восстановить пароль']"
    PASSWORD_RECOVER_HEADER = By.XPATH, ".//h2[text() = 'Восстановление пароля']"
    EMAIL_PLACEHOLDER = By.XPATH, ".//label[text() = 'Email']"
    EMAIL_INPUT_ACTIVE = By.CLASS_NAME, 'input pr-6 pl-6 input_type_text input_size_default input_status_active'
    EMAIL_INPUT = By.NAME, 'name'
    RECOVERY_BUTTON = By.XPATH, ".//button[text() = 'Восстановить']"
    INPUT_CODE = By.XPATH, ".//label[text() = 'Введите код из письма']"
    EYE_SIGN_HIDE = By.XPATH, ".//div[contains(@class, 'icon-action')]"
    PASSWORD_INPUT = By.NAME, 'Введите новый пароль'
    PASSWORD_FIELD = By.XPATH, ".//div[contains(@class, 'input_type_password')]"

