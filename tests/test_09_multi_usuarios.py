import pytest
import allure
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("user_name", ["standard_user", "problem_user", "performance_glitch_user"])
@allure.title("Misión 09: Login Múltiple")

def test_multi_user(page: Page, user_name):
    login = LoginPage(page)
    page.goto("https://www.saucedemo.com/")

    with allure.step(f"Introducir credenciales user 1 {user_name}"):
        login.enter_app(user_name, "secret_sauce")

    with allure.step("Veroficar acceso usuario 1"):
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
