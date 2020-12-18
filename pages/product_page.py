from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_newyear_promo(self):
        assert '?promo=newYear' in self.browser.current_url, 'there is no ?promo=newYear in URI'
 
    def should_be_the_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LOCATOR).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, 'proct price in basket and product price are differents'

    def should_be_alert_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_IN_BASKET)

