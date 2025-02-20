from pages.order_page import OrderPage
import allure


@allure.story("Проверяет функции ленты заказов")
class TestOrderPage:
    @allure.step("Проверяет открытие всплывающего окна с деталями по клику на заказ")
    def test_open_window_after_click_on_order_element(self, home_page):
        home_page.click_on_list_orders()
        order_page = OrderPage(home_page.driver)
        order_page.click_on_order_element()
        order_page.check_open_window_after_click_on_order_element()


    @allure.step("Проверяет, что при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_more_value_counter_after_create_order_for_all_time(self, login):
        order_page = OrderPage(login.driver)
        order_page.click_on_list_orders()
        counter_before_order = order_page.fix_the_counter_value_before_create_order() #записываем количество закзаов до совершения заказа
        order_page.click_on_constructor()
        order_page.drag_element()
        order_page.click_on_button_place_an_order()
        order_page.check_is_place_an_order()
        order_page.click_on_button_close_id_window()
        order_page.click_on_list_orders()
        counter_after_order = order_page.fix_the_counter_value_after_create_order() #записываем количество закзаов после заказа
        assert counter_before_order < counter_after_order


    @allure.step("Проверяет, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_more_value_counter_after_create_order_for_day(self, login):
        order_page = OrderPage(login.driver)
        order_page.click_on_list_orders()
        counter_before_order = order_page.fix_the_counter_value_before_create_order_for_day() #записываем количество закзаов до совершения заказа
        order_page.click_on_constructor()
        order_page.drag_element()
        order_page.click_on_button_place_an_order()
        order_page.check_is_place_an_order()
        order_page.click_on_button_close_id_window()
        order_page.click_on_list_orders()
        counter_after_order = order_page.fix_the_counter_value_after_create_order_for_day() #записываем количество закзаов после заказа
        assert counter_before_order < counter_after_order


    @allure.step("Проверяет, что после оформления заказа его номер появляется в разделе В работе")
    def test_id_after_create_order_is_status_reading(self, login):
        order_page = OrderPage(login.driver)
        order_page.click_on_constructor()
        order_page.drag_element()
        order_page.click_on_button_place_an_order()
        order_page.check_is_place_an_order()
        id_ord = order_page.get_id_order_after_create_order()
        order_page.click_on_button_close_id_window()
        order_page.click_on_list_orders()
        id_reading = order_page.get_id_order_after_create_order_is_reading()
        assert id_ord == id_reading


    @allure.step("Проверяет, что заказ пользователя из раздела «История заказов» отображается на странице «Лента заказов»")
    def test_order_user_visio_in_feed_order(self, login):
        order_page = OrderPage(login.driver)
        order_page.click_on_constructor()
        order_page.drag_element()
        order_page.click_on_button_place_an_order()
        order_page.check_is_place_an_order()
        order_page.click_on_button_close_id_window()
        order_page.click_on_list_orders()
        id_feed_order = order_page.get_id_order_of_story_order()
        order_page.click_on_profile_button()
        order_page.click_on_story_orders_button()
        id_in_story_order = order_page.get_id_order_of_story_order()
        assert id_in_story_order == id_feed_order







