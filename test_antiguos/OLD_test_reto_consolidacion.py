from playwright.sync_api import sync_playwright, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_reto_consolidacion ():
    with sync_playwright()as p:
        browser = p.chromium.launch(headless= False, slow_mo=1000)

        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        login = LoginPage(page)
        Inventory = InventoryPage(page)
        cart = CartPage(page)
        Checkout = CheckoutPage(page)

        login.enter_app("standard_user" ,"secret_sauce")
        Inventory.add_tshirt()
        expect(Inventory.remove_tshirt_btn).to_have_text("Remove")
        Inventory.remove_tshirt()
        expect(Inventory.tshirt_btn).to_have_text("Add to cart")
        Inventory.add_tshirt()
        Inventory.go_to_cart()
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")
        cart.proceed_to_checkout()
        Checkout.fill_shipping_info("Salvador","Ceballos","21110")
        Checkout.click_cancel_()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


if __name__ == "__main__":
    test_reto_consolidacion()