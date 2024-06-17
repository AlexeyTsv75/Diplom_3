from selenium.webdriver.common.by import By


class ProfileLocator:
    EXIT_PROFILE_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ORDER_HISTORY = By.XPATH, ".//a[text() = 'История заказов']"
    LAST_ORDER = By.XPATH, ".//ul[contains(@class, 'OrderHistory_list__')]/li[last()]//p[contains(@class, 'digits')]"
