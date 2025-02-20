import allure
from pages.recovery_password_page import RecoveryPasswordPage
from pages.profile_page import ProfilePage


@allure.story("Проверка функционала восстановления пароля")
class TestRecoveryPasswordPage:
    @allure.title("Проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_transition_on_recovery_password_button(self, home_page):
        recovery_password_page = RecoveryPasswordPage(home_page.driver)
        profile_page = ProfilePage(home_page.driver)
        profile_page.click_on_profile_button()
        recovery_password_page.click_on_recovery_password_button()
        recovery_password_page.check_transition_after_click_on_recovery_password_button()

    @allure.title("Проверяет переход на страницу сброса пароля по кнопке «Восстановить»")
    def test_input_email_and_click_on_recovery_button(self, home_page):
        recovery_password_page = RecoveryPasswordPage(home_page.driver)
        profile_page = ProfilePage(home_page.driver)
        profile_page.click_on_profile_button()
        recovery_password_page.click_on_recovery_password_button()
        recovery_password_page.input_email_for_recovery_password()
        recovery_password_page.click_on_recovery_password_button_second()
        recovery_password_page.check_transition_after_click_on_recovery_password_button_second()

    @allure.title("Проверяет, что поле ввода пароля при нажатии на «отобразить пароль» стало активным")
    def test_active_after_click_on_eye_password(self, home_page):
        recovery_password_page = RecoveryPasswordPage(home_page.driver)
        profile_page = ProfilePage(home_page.driver)
        profile_page.click_on_profile_button()
        recovery_password_page.click_on_recovery_password_button()
        recovery_password_page.input_email_for_recovery_password()
        recovery_password_page.click_on_recovery_password_button_second()
        recovery_password_page.click_on_recovery_eye_button()
        recovery_password_page.check_active_password_phold()