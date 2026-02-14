import allure
from pages.profile_page import ProfilePage


@allure.story("Проверка основного функционала личного кабинета")
class TestProfilePage:
    @allure.title("Проверяет переход по клику на «Личный кабинет»")
    def test_transition_on_profile_button(self, home_page):
        profile_page = ProfilePage(home_page.driver)
        profile_page.click_on_profile_button()
        profile_page.check_transition_after_click_on_profile_button()

    @allure.title("Проверяет переход в раздел «История заказов»")
    def test_transition_on_story_orders(self, login):
        profile_page = ProfilePage(login.driver)
        profile_page.click_on_profile_button()
        profile_page.click_on_story_orders_button()
        profile_page.check_transition_after_click_on_story_orders()

    @allure.title("Проверяет переход по клику на «Выход»")
    def test_transition_on_exit_button(self, login):
        profile_page = ProfilePage(login.driver)
        profile_page.click_on_profile_button()
        profile_page.click_on_exit_button()
        profile_page.check_transition_after_click_on_exit_button()