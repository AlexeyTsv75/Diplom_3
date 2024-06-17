import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import allure


@allure.step('Загружаем driver')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = Options()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()
