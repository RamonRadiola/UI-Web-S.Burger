import pytest
from selenium import webdriver
from pages.home_page import HomePage
from locators import Locators
import requests
from constants import Constants


class WebDriverFactory:
    @staticmethod
    def create_driver(browser_name):
        """
        Создает драйвер для указанного браузера.
        :param browser_name: Имя браузера (chrome, firefox)
        :return: Экземпляр драйвера
        """
        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

# Фикстура для создания и удаления пользователя через API
@pytest.fixture(scope="function")
def api_user():
    # Данные для регистрации пользователя
    user_data = {
        "email": "romastepanov16333_tests@yandex.ru",
        "password": "VpiWU6vpa",
        "name": "TestUser"  # Имя можно задать любое
    }

    # Создаем пользователя через API
    register_response = requests.post(Constants.URL_USER_REG, json=user_data)
    access_token = register_response.json().get("accessToken")

    # Возвращаем данные пользователя и токен
    yield user_data, access_token

    # Удаляем пользователя после завершения теста
    requests.delete(Constants.URL_USER_DATA_CHANGE, headers={"Authorization": access_token})

# Добавляем параметр командной строки для выбора браузера
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Укажите браузер: chrome или firefox",
    )

# Фикстура для драйвера
@pytest.fixture(scope="function")
def driver(request):
    # Получаем значение параметра --browser
    browser_name = request.config.getoption("--browser")

    # Создаем драйвер с помощью фабрики
    driver = WebDriverFactory.create_driver(browser_name)

    # Возвращаем драйвер
    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()

# Фикстура для страницы HomePage
@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    page.go_to_site(driver)
    return page

# Фикстура для логина через UI
@pytest.fixture(scope="function")
def login(home_page, api_user):
    # Логинимся через UI, используя фиксированные email и пароль
    home_page.click_elements(Locators.BUTTON_PROFILE)
    home_page.input_password("VpiWU6vpa")  # Используем фиксированный пароль
    home_page.input_email("romastepanov16333_tests@yandex.ru")  # Используем фиксированный email
    home_page.click_elements(Locators.BUTTON_PROFILE_IN)
    home_page.find_element_for_visio(Locators.SIGNAL_ASSEMBLY_BURGER)
    return home_page



# import pytest
# from selenium import webdriver
# from pages.home_page import HomePage
# from locators import Locators
#
# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
# @pytest.fixture(scope="function")
# def home_page(driver):
#     page = HomePage(driver)
#     page.go_to_site(driver)
#     return page
#
#
# @pytest.fixture(scope="function")
# def login(home_page):
#     home_page.click_elements(Locators.BUTTON_PROFILE)
#     home_page.input_password('VpiWU6v')  # Передаем пароль напрямую
#     home_page.input_email('romastepanov16333@yandex.ru')  # Передаем email напрямую
#     home_page.click_elements(Locators.BUTTON_PROFILE_IN)
#     home_page.find_element_for_visio(Locators.SIGNAL_ASSEMBLY_BURGER)
#     return home_page