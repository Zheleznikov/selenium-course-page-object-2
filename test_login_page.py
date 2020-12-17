from pages.login_page import LoginPage
from pages.locators import Urls


def test_guest_should_see_login_page(browser):
    login_page = LoginPage(browser, Urls.LOGIN_PAGE_URL)
    login_page.open()
    login_page.should_be_login_page()
