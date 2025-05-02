import allure
import pytest

from pages.cart_page import CartPage


@pytest.mark.parametrize('product_in_cart', [
    (45, 1),
], indirect=True)
def test_cart_contains_product(auth_token, product_in_cart):
    with allure.step("Открытие страницы корзины"):
        cart_page = CartPage(auth_token)
        cart_page.open()

    with allure.step("Получение элементов корзины"):
        cart_items = cart_page.get_cart_items()

    with allure.step("Проверка наличия товара в корзине"):
        assert len(cart_items) > 0

    with allure.step("Удаление товара из корзины"):
        cart_page.set_cart_quantity(0)


@pytest.mark.parametrize('product_in_cart', [
    (45, 100)
], indirect=True)
def test_cart_clear(auth_token, product_in_cart):
    with allure.step("Открытие страницы корзины"):
        cart_page = CartPage(auth_token)
        cart_page.open()

    with allure.step("Удаление товара из корзины"):
        cart_page.set_cart_quantity(0)

    with allure.step("Проверка, что корзина пуста"):
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 0
