import allure
import requests
import os

from utils.attach import attach_text

LOGIN_URL = f"{os.getenv('BASE_URL')}/login"
EMAIL = os.getenv("LOGIN_EMAIL")
PASSWORD = os.getenv("LOGIN_PASSWORD")


@allure.step("Получение auth cookie")
def get_auth_cookie():
    payload = {
        "Email": EMAIL,
        "Password": PASSWORD,
        "RememberMe": True,
    }

    with allure.step("Отправка POST-запроса для логина"):
        response = requests.post(LOGIN_URL, data=payload, allow_redirects=False)

        attach_text("Request",
                    f"URL: {LOGIN_URL}\nMethod: POST\nPayload: {payload}\nHeaders: {response.request.headers}")
        attach_text("Response", response.text)

    if response.status_code != 302:
        raise Exception()

    auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    if not auth_cookie:
        raise Exception()

    attach_text("Auth Cookie", auth_cookie)
    return auth_cookie
