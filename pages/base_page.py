from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    @allure.step("базовый метод с переходом на главную старницу сайта")
    def go_to_site(self, driver):
        self.driver.get(self.url)
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_PROFILE))

    @allure.step("базовый метод определения кликабельности элемента")
    def find_element_for_click(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not find element {locator}')

    @allure.step("Клик по элементу")
    def click_elements(self, locator):
        self.find_element_for_click(locator).click()

    @allure.step("базовый метод для определения появления элемента'")
    def find_element_for_visio(self, locator, time=50):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step("Метод прокрутки страницы до нужного элемента")
    def scroll_to_element_base(self, locator):
        element = self.find_element_for_visio(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Возвращает текущий url")
    def check_current_url(self):
        return self.driver.current_url

    @allure.step("ввод email")
    def input_email(self, email):
        self.find_element_for_visio(locator=Locators.PHOLD_EMAIL).send_keys(email)

    @allure.step("ввод password")
    def input_password(self, password):
        self.find_element_for_visio(locator=Locators.PHOLD_PASSWORD).send_keys(password)

    @allure.step("перетаскивание элемента")
    def drag_element(self):
        element_to_drag = self.find_element_for_visio(Locators.BUTTON_FLUORESCENT_BUN)
        target_element = self.find_element_for_visio(Locators.BUTTON_FOLDER)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_to_drag, target_element).perform()