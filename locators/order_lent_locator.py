from selenium.webdriver.common.by import By


class OrderLentLocator:

    LENT_FIRST_ORDER = By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]"
    ORDER_DESCRIPTION_WINDOW = By.XPATH, ".//section[contains(@class, 'opened')]"
    ORDERS = By.XPATH, ".//p[contains(@class, 'digits')]"
    ALL_ORDER = By.XPATH, ".//p[text() = 'Выполнено за все время:']/following-sibling::p"
    TODAY_ORDER = By.XPATH, ".//p[text() = 'Выполнено за сегодня:']/following-sibling::p"
    ORDERS_IN_WORK = By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li"
