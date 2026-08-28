from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_limpiar_carrito(login_ready):
    inventory = InventoryPage(login_ready)
    cart = CartPage(login_ready)

    items_a_limpiar = ["backpack", "bike-light", "bolt-t-shirt", "onesie"]

    for item in items_a_limpiar:
        inventory.add_specific_product(item)

    expect(inventory.cart_icon).to_have_text("4")

    inventory.go_to_cart()
    cart.all_remove_items()

    expect(cart.item_name_label).not_to_be_visible()
    print("Se ha limpiado el carrito correctamente, no hay items en el carrito")            