from playwright.sync_api import sync_playwright
# Importamos tu clase del archivo login_page
from pages.login_page import LoginPage

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # 1. Instanciar (Fabricar el objeto real a partir del molde)
        login = LoginPage(page)
        
        # 2. Usar el objeto
        page.goto("https://www.saucedemo.com")
        login.enter_app("standard_user", "secret_sauce")
        
        print("Login realizado con éxito")
        browser.close()
