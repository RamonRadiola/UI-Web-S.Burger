import pytest
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
import requests
from constants import Constants
from webdriver_factory import WebDriverFactory
from data import TestUser


# Фикстура для создания и удаления пользователя через API
@pytest.fixture(scope="function")
def api_user():
    # Данные для регистрации пользователя
    user_data = {
        "email": TestUser.EMAIL,
        "password": TestUser.PASSWORD,
        "name": TestUser.NAME
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
    browser_name = request.config.getoption("--browser")
    driver = WebDriverFactory.create_driver(browser_name)
    yield driver
    driver.quit()

# Фикстура для страницы HomePage
@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    page.go_to_site(driver)
    return page

# Фикстура для страницы ProfilePage
@pytest.fixture(scope="function")
def profile_page(driver):
    page = ProfilePage(driver)
    return page

# Фикстура для логина через UI
@pytest.fixture(scope="function")
def login(home_page, profile_page, api_user):
    profile_page.click_on_profile_button()
    profile_page.input_password()
    profile_page.input_email()
    profile_page.click_on_in_button()
    profile_page.waiting_for_menu_item_to_appear_construction()
    return profile_page