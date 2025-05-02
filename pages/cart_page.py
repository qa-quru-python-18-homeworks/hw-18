import os
import time

from selene import browser, query


class CartPage:
    base_url = f"{os.getenv('BASE_URL')}/cart"
    cart_item = ".cart-item-row"
    cart_quantity = ".qty-input"

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def open(self):
        browser.open(self.base_url)
        browser.driver.add_cookie({
            'name': 'NOPCOMMERCE.AUTH',
            'value': self.auth_token,
        })
        browser.driver.refresh()

    def get_cart_items(self):
        time.sleep(0.3)
        return browser.all(self.cart_item)

    def get_cart_quantity(self):
        return browser.element(self.cart_quantity).get(query.attribute("value"))

    def set_cart_quantity(self, quantity):
        browser.element(self.cart_quantity).clear().type(quantity).press_enter()
