from pages.base_page import BasePage
from locators import Locators
import allure


class HomePage(BasePage):
    @allure.step("Клик по кнопке «Конструктор»")
    def click_on_constructor(self):
        return self.find_element_for_click(locator=Locators.BUTTON_CONSTRUCTION).click()

    @allure.step("Проверка перехода по клику конструктор")
    def check_transition_on_constructor(self):
        assert 'Соберите бургер' in self.find_element_for_visio(Locators.SIGNAL_ASSEMBLY_BURGER).text

    @allure.step("Клик по «Лента заказов»")
    def click_on_list_orders(self):
        return self.find_element_for_click(locator=Locators.BUTTON_LIST_ORDERS).click()

    @allure.step("")
    def check_transition_list_orders(self):
        assert 'Лента заказов' in self.find_element_for_visio(Locators.SIGNAL_LIST_ORDERS).text

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self):
        return self.find_element_for_click(locator=Locators.BUTTON_FLUORESCENT_BUN).click()

    @allure.step("Проверка появления окна с подробностями ингредиента")
    def check_visio_ingredient_window(self):
        assert self.find_element_for_visio(Locators.SIGNAL_FLUORESCENT_BUN)

    @allure.step("Клик на кнопку закрытия окна")
    def click_on_button_close_ingredient_window(self):
        return self.find_element_for_click(locator=Locators.BUTTON_CLOSE_FLUORESCENT_BUN).click()

    @allure.step("Проверка закрытия окна")
    def check_closed_ingredient_window(self):
        assert self.find_element_for_visio(Locators.SIGNAL_AFTER_CLOSE_FLUORESCENT_BUN)

    @allure.step("Проверка счетчика заказов")
    def check_is_counter(self):
        assert '2' in self.find_element_for_visio(Locators.COUNTER_FLUORESCENT_BUN).text

    @allure.step("Клик на «Оформить»")
    def click_on_button_place_an_order(self):
        return self.find_element_for_click(locator=Locators.BUTTON_PLACE_AN_ORDER).click()

    @allure.step("Проверка после нажатия на «Оформить»")
    def check_is_place_an_order(self):
        assert 'Ваш заказ начали готовить' in self.find_element_for_visio(Locators.SIGNAL_PLACE_AN_ORDER).text