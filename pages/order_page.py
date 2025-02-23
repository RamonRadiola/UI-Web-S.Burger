from pages.base_page import BasePage
from locators import Locators
import allure


class OrderPage(BasePage):
    @allure.step("Клик по заказу")
    def click_on_order_element(self):
        return self.click_elements(locator=Locators.ORDER_FEED_ELEMENT_UP)

    @allure.step("Проверка появления окна с подробностями заказа")
    def check_open_window_after_click_on_order_element(self):
        assert self.find_element_for_visio(Locators.ORDER_FEED_WINDOW)

    @allure.step("Получаем цифры счетчика за все время")
    def get_counter_orders_for_all_time(self):
        return self.find_element_for_visio(locator=Locators.COUNTER_COMPLETED_FOR_ALL_TIME).text

    @allure.step("Получаем цифры счетчика за все сегодня")
    def get_counter_orders_for_day(self):
        return self.find_element_for_visio(locator=Locators.COUNTER_COMPLETED_FOR_TODAY).text

    @allure.step("Получаем цифры идентификатора после оформления заказа")
    def get_id_order_after_create_order(self):
        self.wait_of_element_for_invisibility(Locators.BOX_V)
        id = self.find_element_for_visio(locator=Locators.ID_AFTER_CREATE_ORDER).text
        return int(id)

    @allure.step("Клик на кнопку закрытия окна совершенного заказа")
    def click_on_button_close_id_window(self):
        self.wait_of_element_for_invisibility(Locators.BOX_V)
        return self.find_element_for_click(locator=Locators.BUTTON_CLOSE_ID_ORDER).click()

    @allure.step("Проверяем присвоение нового идентификатора после оформления заказа")
    def check_create_new_id_after_create_order(self):
        order_id = self.get_id_order_after_create_order()
        return int(order_id) != 9999

    @allure.step("Фиксируем значение счетчика за все время до оформления заказа")
    def fix_the_counter_value_before_create_order(self):
        counter_full_before_add = int(self.get_counter_orders_for_all_time())  # считываем количество заказов до совершения заказа
        return counter_full_before_add

    @allure.step("Фиксируем значение счетчика за все время после оформления заказа")
    def fix_the_counter_value_after_create_order(self):
        counter_full_after_add = int(self.get_counter_orders_for_all_time())  # считываем количество заказов после совершения заказа
        return counter_full_after_add

    @allure.step("Фиксируем значение счетчика за день до оформления заказа")
    def fix_the_counter_value_before_create_order_for_day(self):
        counter_full_before_add = int(self.get_counter_orders_for_day())  # считываем количество заказов до совершения заказа
        return counter_full_before_add

    @allure.step("Фиксируем значение счетчика за день после оформления заказа")
    def fix_the_counter_value_after_create_order_for_day(self):
        counter_full_before_add = int(self.get_counter_orders_for_day())  # считываем количество заказов после совершения заказа
        return counter_full_before_add

    @allure.step("Получаем цифры идентификатора заказа из раздела В работе")
    def get_id_order_after_create_order_is_reading(self):
        id = int(self.find_element_for_visio(locator=Locators.ID_IN_READING).text)
        return id

    @allure.step("Получаем цифры идентификатора после оформления заказа")
    def get_id_order_of_story_order(self):
        id = self.find_element_for_visio(locator=Locators.ID_UP_ELEMENT_OF_STORY_ORDER_DIGIT).text
        return id

    @allure.step("Клик по «Лента заказов»")
    def click_on_list_orders(self):
        return self.find_element_for_click(locator=Locators.BUTTON_LIST_ORDERS).click()

    @allure.step("Клик по кнопке «Конструктор»")
    def click_on_constructor(self):
        return self.find_element_for_click(locator=Locators.BUTTON_CONSTRUCTION).click()

    @allure.step("Клик на «Оформить»")
    def click_on_button_place_an_order(self):
        return self.find_element_for_click(locator=Locators.BUTTON_PLACE_AN_ORDER).click()

    @allure.step("Проверка после нажатия на «Оформить»")
    def check_is_place_an_order(self):
        assert 'Ваш заказ начали готовить' in self.find_element_for_visio(Locators.SIGNAL_PLACE_AN_ORDER).text

    @allure.step("Клик по кнопке «Личный кабинет»")
    def click_on_profile_button(self):
        return self.click_elements(locator=Locators.BUTTON_PROFILE)

    @allure.step("Клик по кнопке «История заказов»")
    def click_on_story_orders_button(self):
        return self.click_elements(locator=Locators.BUTTON_PROFILE_STORY_ORDERS)



