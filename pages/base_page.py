from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=6):
        self.browser = browser
        self.url = url
        # self.user_language = user_language
        self.browser.implicitly_wait(timeout)

    def open(self):
        # открываем браузер
        self.browser.get(self.url)
        # print(self.user_language)

    def is_element_present(self, how, what):
        # проверяем есть ли элемент на старнице. Если такого элемента не находится, то подставляем кастомное
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
