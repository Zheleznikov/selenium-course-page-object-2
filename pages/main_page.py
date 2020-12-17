from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        # переход на страницу где лониться
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # проверка что есть кнопка для перехода на страницу логина
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'login link is not presented'
