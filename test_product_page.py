# import pytest
from pages.product_page import ProductPage
# from pages.locators import Urls
from time import sleep

link1 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


# @pytest.mark.parametrize('link', Urls.LINKS_PROMO_OFFER)
def test_guest_can_add_product_to_basket(browser):
    browser.delete_all_cookies()
    product_page = ProductPage(browser, link1)
    product_page.open()
    product_page.go_to_basket()
    product_page.should_be_alert_product_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_the_same_price()
    # sleep(900)