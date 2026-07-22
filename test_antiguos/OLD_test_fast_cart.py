# test_comprar_con_fixture.py
from pages.inventory_page import InventoryPage
# Aquí ya NO importo el LoginPage, porque ya me lo da Pytest masticado

# ¿Ves que en el paréntesis pongo 'login_ready'?
def test_compra_rapida(login_ready):
    # El objeto page es el que sale del yield del conftest
    inventory = InventoryPage(login_ready)

    # ACCIÓN DIRECTA (Sin login, ¡ya estamos dentro!)
    inventory.add_backpack()
    inventory.go_to_cart()