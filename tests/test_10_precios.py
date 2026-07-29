import pytest
import allure
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("producto,precio_esperado",[
    ("Sauce Labs Backpack", "$29.99"),
    ("Sauce Labs Onesie", "$7.99"),
    ("Sauce Labs Bike Light", "$9.99")
])

@allure.title("Mision 10: Comprobador de precios")
def test_comprobador_precios(login_ready, producto, precio_esperado):
    inventory = InventoryPage(login_ready)

    with allure.step(f"Añadir producto: {producto}"):
        # Usamos un truco: Playwright puede buscar por texto parcial
        # Buscamos el botón que contenga el nombre del producto
        login_ready.locator(".inventory_item").filter(has_text=producto).get_by_role("button").click()
    
    with allure.step(f"Verificar que {producto} vale {precio_esperado}"):
        # Buscamos el contenedor que tiene el nombre del producto
        # Y de ese mismo contenedor, sacamos el precio
        contenedor = login_ready.locator(".inventory_item").filter(has_text=producto)
        precio_real = contenedor.locator(".inventory_item_price")
        
        expect(precio_real).to_have_text(precio_esperado)