from pages. inventory_page import InventoryPage, expect

def test_estoy_en_el_carro(login_ready):
    inventory = InventoryPage(login_ready)
    inventory.add_backpack()
    inventory.go_to_cart()
    expect(login_ready).to_have_url("https://www.saucedemo.com/cart.html")
    yield login_ready



# test_estoy_en_el_carro.py
from pages.cart_page import CartPage # Importa el del Carrito!
from playwright.sync_api import expect

# 1. PEDIMOS LA FIXTURE QUE YA TIENE LA MOCHILA (add_backpack)
# NO pidas login_ready, eso es nivel 1. Pide add_backpack (nivel 2).
def test_de_verificacion_carrito(add_backpack):
    
    # 2. El objeto 'add_backpack' ya es el navegador en la URL del carro
    cart = CartPage(add_backpack)

    # 3. Solo verificamos
    expect(add_backpack).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.checkout_btn).to_be_visible()