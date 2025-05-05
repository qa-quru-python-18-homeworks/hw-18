import os

import allure
import requests

from utils.attach import attach_text

ADD_TO_CART_URL = f"{os.getenv('BASE_URL')}/addproducttocart/catalog"


@allure.step("Добавление товара в корзину")
def add_to_cart(product_id, quantity, auth_cookie):
    response = requests.post(f"{ADD_TO_CART_URL}/{product_id}/1/{quantity}", cookies={"NOPCOMMERCE.AUTH": auth_cookie})

    attach_text("Request",
                f"URL: {ADD_TO_CART_URL}/{product_id}/1/{quantity}\nMethod: POST\nHeaders: {response.request.headers}")
    attach_text("Response", response.text)
