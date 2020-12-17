from pages.main_page import MainPage
from pages.locators import Urls


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, Urls.MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, Urls.MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()