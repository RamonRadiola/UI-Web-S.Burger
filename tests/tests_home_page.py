import allure


@allure.story("Проверка основного функционала главной страницы")
class TestHomePage:
    @allure.title("Проверяет переход по клику на «Конструктор»")
    def test_transition_on_constructor(self, home_page):
        home_page.click_on_list_orders()
        home_page.click_on_constructor()
        home_page.check_transition_on_constructor()

    @allure.title("Проверет переход по клику на «Лента заказов»")
    def test_transition_list_orders(self, home_page):
        home_page.click_on_list_orders()
        home_page.check_transition_list_orders()

    @allure.title("Проверка появления всплывающего окна с деталями после клика на ингредиент")
    def test_check_visio_ingredient_window_after_click(self, home_page):
        home_page.click_on_ingredient()
        home_page.check_visio_ingredient_window()

    @allure.title("Проверка закрытия всплывающего окна кликом по крестику")
    def test_closed_ingredient_window_after_click(self, home_page):
        home_page.click_on_ingredient()
        home_page.click_on_button_close_ingredient_window()
        home_page.check_closed_ingredient_window()

    @allure.title("Проверка увеличения каунтера при добавлении ингредиента в заказ")
    def test_drag_element(self, home_page):
        home_page.drag_element()
        home_page.check_is_counter()

    @allure.title("Проверка возможности оформления заказа залогиненным пользователем")
    def test_place_an_order(self, login, home_page):
        home_page.drag_element()
        home_page.click_on_button_place_an_order()
        home_page.check_is_place_an_order()