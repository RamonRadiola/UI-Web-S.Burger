from selenium.webdriver.common.by import By


class Locators:
    BUTTON_LIST_ORDERS = (By.XPATH, '//*[contains(@class, "AppHeader_header__linkText__3q_va ml-2") and text()="Лента Заказов"]')
    SIGNAL_LIST_ORDERS = (By.XPATH, '//*[@class="text text_type_main-large mt-10 mb-5"]')
    BUTTON_CONSTRUCTION = (By.XPATH, '//*[contains(@class, "AppHeader_header__linkText__3q_va ml-2") and text()="Конструктор"]')
    SIGNAL_ASSEMBLY_BURGER = (By.XPATH, '//*[contains(@class, "text text_type_main-large") and text()="Соберите бургер"]')
    BUTTON_FLUORESCENT_BUN = (By.XPATH, '//*[contains(@class, "BurgerIngredient_ingredient") and text()="Флюоресцентная булка R2-D3"]')
    SIGNAL_FLUORESCENT_BUN = (By.XPATH, '//*[contains(@class, "text text_type_main-medium mb-8") and text()="Флюоресцентная булка R2-D3"]')
    BUTTON_CLOSE_FLUORESCENT_BUN = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button')
    SIGNAL_AFTER_CLOSE_FLUORESCENT_BUN = (By.XPATH, '//*[contains(@class, "text text_type_main-default") and text()="Начинки"]') #пока не станет кликабельным
    COUNTER_FLUORESCENT_BUN = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p')
    BUTTON_RECOVER_PASSWORD = (By.XPATH, '//*[contains(@class, "Auth_link__1fOlj") and text()="Восстановить пароль"]')
    BUTTON_RECOVER_PASSWORD_SECOND = (By.XPATH, '//*[contains(@class, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa") and text()="Восстановить"]')
    BUTTON_EYE = (By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > div > svg")
    BUTTON_PROFILE = (By.XPATH, '//*[contains(@class, "AppHeader_header__linkText__3q_va ml-2") and text()="Личный Кабинет"]')
    BUTTON_PROFILE_STORY_ORDERS = (By.XPATH, '//*[contains(@class, "Account_link") and text()="История заказов"]')
    BUTTON_PROFILE_EXIT = (By.XPATH, '//*[contains(@class, "Account_button") and text()="Выход"]')
    BUTTON_PROFILE_IN = (By.XPATH, '//*[contains(@class, "button_button") and text()="Войти"]') #сигнал после нажатия на кнопку "выход"
    BUTTON_PLACE_AN_ORDER = (By.XPATH, '//*[contains(@class, "button_button__33qZ0") and text()="Оформить заказ"]')
    SIGNAL_PLACE_AN_ORDER = (By.XPATH, '//*[contains(@class, "undefined text text_type_main-small mb-2") and text()="Ваш заказ начали готовить"]')


    PHOLD_EMAIL = (By.XPATH, '//*[@class="text input__textfield text_type_main-default" and @type="text"]')
    PHOLD_PASSWORD = (By.XPATH, '//*[@class="text input__textfield text_type_main-default" and @type="password"]')
    PHOLD_PASSWORD_ACTIVE = (By.XPATH, '//*[@class="text input__textfield text_type_main-default" and @type="text"]')


    BUTTON_FOLDER = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')  #куда перетаскивать ингредиенты для совершения заказа
    ORDER_FEED_ELEMENT_UP = (By.XPATH, '//*[@class="OrderHistory_listItem__2x95r mb-6"][1]')
    ORDER_FEED_WINDOW = (By.XPATH, '//*[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]') #окно с проверкой после нажатия на заказ в ленте


    BEFORE_COMPLETED_FOR_ALL_TIME = (By.XPATH, '//*[contains(@class, "text text_type_main-medium") and text()="Выполнено за все время:"]')
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, '//*[contains(@class, "text text_type_main-medium") and text()="Выполнено за все время:"]/following-sibling::p[1]')
    BEFORE_COMPLETED_FOR_TODAY = (By.XPATH, '//*[contains(@class, "text text_type_main-medium") and text()="Выполнено за сегодня:"]')
    COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, '//*[contains(@class, "text text_type_main-medium") and text()="Выполнено за сегодня:"]/following-sibling::p[1]')

    ID_AFTER_CREATE_ORDER = (By.XPATH, '//*[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]') #отсюда достать цифры номера заказа ПОСЛЕ ОФОРМЛЕНИЯ
    ID_IN_READING = (By.XPATH, '//*[@class ="text text_type_digits-default mb-2"]') #отсюда достать цифры номера заказа В РАБОТЕ
    ID_UP_ELEMENT_OF_STORY_ORDER_MB = (By.XPATH, '//*[@class="text text_type_digits-default mb-10 mt-5"]') #отсюда достать цифры номера заказа &&&&&&
    # ID_UP_ELEMENT_OF_STORY_ORDER = (By.XPATH, '//*[@class="OrderHistory_listItem__2x95r mb-6"][1]') #отсюда достать цифры номера заказа В ИСТОРИИ ЗАКАЗОВ/ЛЕНТЕ ЗАКАЗОВ
    ID_UP_ELEMENT_OF_STORY_ORDER_DIGIT = (By.XPATH, '//*[@class="text text_type_digits-default"]') #отсюда достать цифры номера заказа В ИСТОРИИ ЗАКАЗОВ/ЛЕНТЕ ЗАКАЗОВ

    BUTTON_CLOSE_ID_ORDER = (By.CSS_SELECTOR, "#root > div > section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 > div.Modal_modal__container__Wo2l_ > button > svg")
    BOX_V = (By.CLASS_NAME, 'Modal_modal__loading__3534A') #модуль, мешающий нажатию на закрытие всплывающего окна после совершения заказа


