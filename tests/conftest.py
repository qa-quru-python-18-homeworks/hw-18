import pytest
from selene import browser

from api.auth_api import get_auth_cookie
from api.cart_api import add_to_cart


@pytest.fixture(scope="session")
def auth_token():
    return get_auth_cookie()


@pytest.fixture()
def product_in_cart(auth_token, request):
    product_id, quantity = request.param
    add_to_cart(product_id, quantity, auth_token)


@pytest.fixture(scope="session", autouse=True)
def maximize_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()
