from pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()