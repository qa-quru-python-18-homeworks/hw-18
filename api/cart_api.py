import os

import allure
import requests

ADD_TO_CART_URL = f"{os.getenv('BASE_URL')}/addproducttocart/catalog"


@allure.step("Добавление товара в корзину")
def add_to_cart(product_id, quantity, auth_cookie):
    requests.post(f"{ADD_TO_CART_URL}/{product_id}/1/{quantity}", cookies={"NOPCOMMERCE.AUTH": auth_cookie})
