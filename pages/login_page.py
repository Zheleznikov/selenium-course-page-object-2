from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_register_form()
        self.should_be_login_url()
        self.should_be_login_url()

    def should_be_login_url(self):
        # проверка что в url есть слово логин
        assert "/login" in self.browser.current_url, 'word "login" not in url'

    def should_be_login_form(self):
        # проверка, что на странице есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "login form is not presented"

    def should_be_register_form(self):
        # проверка что на странице есть форма регистрации
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "register form is not presented"
