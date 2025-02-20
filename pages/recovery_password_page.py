from pages.base_page import BasePage
from locators import Locators
from constants import Constants
import allure


class RecoveryPasswordPage(BasePage):
    @allure.step("Клик по кнопке «Восстановить пароль»")
    def click_on_recovery_password_button(self):
        return self.click_elements(locator=Locators.BUTTON_RECOVER_PASSWORD)

    @allure.step("Проверка перехода после клика на «Восстановить пароль»")
    def check_transition_after_click_on_recovery_password_button(self):
        assert self.check_current_url() == Constants.URL_FORGOT_PASSWORD

    @allure.step("Ввод email»")
    def input_email_for_recovery_password(self):
        self.input_email('romastepanov16333_tests@yandex.ru')

    @allure.step("Клик по кнопке «Восстановить»")
    def click_on_recovery_password_button_second(self):
        return self.click_elements(locator=Locators.BUTTON_RECOVER_PASSWORD_SECOND)

    @allure.step("Проверка перехода после клика на «Восстановить»")
    def check_transition_after_click_on_recovery_password_button_second(self):
        self.find_element_for_visio(Locators.PHOLD_PASSWORD)
        assert self.check_current_url() == Constants.URL_RESET_PASSWORD

    @allure.step("Клик по кнопке «Отобразить пароль»")
    def click_on_recovery_eye_button(self):
        return self.click_elements(locator=Locators.BUTTON_EYE)

    @allure.step("Проверка, что поля для ввода пароля стало активным")
    def check_active_password_phold(self):
        assert self.find_element_for_visio(Locators.PHOLD_PASSWORD_ACTIVE) == self.driver.switch_to.active_element

