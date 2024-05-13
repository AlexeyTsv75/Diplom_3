from selenium.webdriver.common.by import By


class IngredientLocator:
    FLU_BUN_ING = By.XPATH, ".//h2[text() = 'Детали ингредиента']"
    X_CLOSE_ING = By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
