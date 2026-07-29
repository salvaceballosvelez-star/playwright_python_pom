import json
import allure
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_login_desde_json(page: Page):
    # 1. Abrimos el archivo
    with open("data.json") as f:
        datos = json.load(f) # PISTA: librería 'json', método 'load'

    # 2. Sacamos los datos de las etiquetas del JSON
    user_json = datos["login"]["user"]
    pass_json = datos["login"]["pass"]

    # 3. Ejecutamos el login
    login = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    
    login.enter_app(user_json,pass_json) # PISTA: Usa las variables de arriba

    # 4. Verificamos
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")