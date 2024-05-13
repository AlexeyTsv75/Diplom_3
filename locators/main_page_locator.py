from selenium.webdriver.common.by import By


class MainPageLocator:
    LOGIN_ACC_BUTTON = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    PROFILE_BUTTON = By.XPATH, ".//p[text() = 'Личный Кабинет']"
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[text() = 'Оформить заказ']"
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text() = 'Конструктор']"
    SET_BURGER_HEADER = By.XPATH, ".//h1[text() = 'Соберите бургер']"
    ORDER_LENT_BUTTON = By.XPATH, ".//p[text() = 'Лента Заказов']"
    ORDER_LENT_HEADER = By.XPATH, ".//h1[text() = 'Лента заказов']"
    FLU_BUN = By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"
    FILLING_BUTTON = By.XPATH, ".//span[text() = 'Начинки']"
    FLU_BUN_COUNTER = By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']/preceding-sibling::div/p"
    YOUR_ORDER_IS_COCKING = By.XPATH, ".//p[text() = 'Ваш заказ начали готовить']"
    ORDER_NUMBER = (By.XPATH,
                    ".//h2[@class = "
                    "'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    X_CLOSE = By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    FLU_BUN_ING = By.XPATH, ".//h2[text() = 'Детали ингредиента']"
    X_CLOSE_ING = By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
