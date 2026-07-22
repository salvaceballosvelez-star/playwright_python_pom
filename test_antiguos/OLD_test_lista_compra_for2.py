from playwright.sync_api import sync_playwright , expect
from pages.inventory_page import InventoryPage

def test_comprar_todo(login_ready):
    
    inventory = InventoryPage(login_ready)
    compras = ["backpack", "bike-light", "onesie"]

    for items in compras:
        inventory.add_specific_product(items)
    expect(inventory.cart_icon).to_have_text("3")