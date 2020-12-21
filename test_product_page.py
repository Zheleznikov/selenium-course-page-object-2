import pytest
from pages.product_page import ProductPage
from pages.locators import Urls
from time import sleep

testing_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.parametrize("link", Urls.LINKS_PROMO_OFFER)
# @pytest.mark.parametrize('link', ["okay_link",
#                                   pytest.param("bugged_link", marks=pytest.mark.xfail),
#                                   "okay_link"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_name_and_price()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_alert_that_product_add_to_basket()
    product_page.should_be_alert_with_basket_price()
    product_page.is_product_price_the_same()
    product_page.is_product_name_the_same()
    sleep(600)


@pytest.mark.xfail(reason="guest see message after adding")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, testing_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()
    sleep(20)


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, testing_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="succes message doesnt dissapear")
def test_message_dissapeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, testing_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.success_message_should_dissapear()
