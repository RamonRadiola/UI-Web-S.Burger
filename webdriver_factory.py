from selenium import webdriver

class WebDriverFactory:
    @staticmethod
    def create_driver(browser_name):
        """
        Создает драйвер для указанного браузера.
        :param browser_name: Имя браузера (chrome, firefox)
        :return: Экземпляр драйвера
        """
        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")