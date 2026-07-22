#**Llamada a las herramientas:** Importa `sync_playwright` y `expect`.
from playwright.sync_api import sync_playwright, expect

#**Llamada a tus especialistas:** Importa las 5 clases que tienes en la carpeta `pages`. (Usa la sintaxis: `from pages.nombre_archivo import NombreClase`)

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.overview_page import OverViewPage

#**Crea la función del test:** Llámala `def test_full_purchase_flow():`.

def test_full_purchase_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)

    #Creamos una PESTAÑA (page) dentro de ese browser
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")  

        login = LoginPage(page)
        inventory = InventoryPage(page)
        cart = CartPage(page)
        Checkout = CheckoutPage(page)
        OverView = OverViewPage(page)

        login.enter_app("standard_user" ,"secret_sauce")
        inventory.add_backpack()
        inventory.go_to_cart()
        cart.proceed_to_checkout()
        Checkout.fill_shipping_info("Salvador", "Ceballos", "21110")
        OverView.finish_shopping()

if __name__ == "__main__":
    test_full_purchase_flow()




