from selenium.webdriver.common.by import By


class Urls():
    MAIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_PAGE_URI = '/accounts/login/'


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')