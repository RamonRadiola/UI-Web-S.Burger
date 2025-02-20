from pages.home_page import HomePage
from locators import Locators
from constants import Constants
import allure


class ProfilePage(HomePage):
    @allure.step("Клик по кнопке «Личный кабинет»")
    def click_on_profile_button(self):
        return self.click_elements(locator=Locators.BUTTON_PROFILE)

    @allure.step("Проверка перехода после клика на «Личный кабинет»")
    def check_transition_after_click_on_profile_button(self):
        assert self.check_current_url() == Constants.URL_LOGIN

    @allure.step("Клик по кнопке «История заказов»")
    def click_on_story_orders_button(self):
        return self.click_elements(locator=Locators.BUTTON_PROFILE_STORY_ORDERS)

    @allure.step("Проверка перехода после клика на «История заказов»")
    def check_transition_after_click_on_story_orders(self):
        assert self.check_current_url() == Constants.URL_STORY_ORDERS

    @allure.step("Клик по кнопке «Выход»")
    def click_on_exit_button(self):
        self.click_elements(locator=Locators.BUTTON_PROFILE_EXIT)
        return self.find_element_for_click(Locators.BUTTON_PROFILE_IN)

    @allure.step("Проверка выполнения выхода после клика на «Выход»")
    def check_transition_after_click_on_exit_button(self):
        assert self.check_current_url() == Constants.URL_LOGIN