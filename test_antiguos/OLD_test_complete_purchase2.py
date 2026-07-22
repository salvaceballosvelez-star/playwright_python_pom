from playwright.sync_api import sync_playwright, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverViewPage

def test_full_happy_path():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo=1000)

        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        login = LoginPage(page)
        inventory = InventoryPage(page)
        cart = CartPage (page)
        Checkout = CheckoutPage(page) 
        OverView = OverViewPage (page)


        login.enter_app("standard_user" ,"secret_sauce")
        inventory.add_backpack()
        inventory.go_to_cart()
        cart.proceed_to_checkout()
        Checkout.fill_shipping_info("Salvador", "Ceballos", "21110")
        OverView.finish_shopping()

    
if __name__ == "__main__":
    test_full_happy_path()