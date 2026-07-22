from playwright.sync_api import expect
from pages.inventory_page import InventoryPage

def test_compar_item1(login_ready):
    inventory = InventoryPage(login_ready)

    inventory.add_backpack()
    expect(login_ready).to_have_url("https://www.saucedemo.com/inventory.html")
    print("Verificación de Inventario: Éxito")


