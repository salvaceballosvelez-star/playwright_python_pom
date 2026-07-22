# 1. Cambiamos async_api por sync_api
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # El ID correcto en SauceDemo es #user-name, no #username
        self.user_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.error_message_text = page.locator("[data-test='error']")

    def enter_app(self, username:str, password:str):
        # Usamos las variables que entran por el paréntesis (parámetros)
        self.user_field.fill(username)
        self.password_field.fill(password)
        # Click no necesita el selector otra vez, ya lo sabe la variable
        self.login_btn.click()

  