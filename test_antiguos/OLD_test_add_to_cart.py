from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_backpack_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        inventory = InventoryPage(page)

        page.goto("https://www.saucedemo.com")

        login.enter_app("standard_user","secret_sauce")

        inventory.add_backpack()
        inventory.go_to_cart()

        expect(page).to_have_url("https://www.saucedemo.com/cart.html")

        print("Test de mochila completado")
        browser.close()

        
