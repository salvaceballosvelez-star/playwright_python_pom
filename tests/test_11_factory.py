import json
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_fabrica_industrial(page):
    # 1. CARGAR DATOS
    with open("data.json") as f:
        data = json.load(f)

    # 2. LOGIN (Usando el JSON)
    login = LoginPage(page)
    page.goto(data["config"]["url"])
    login.enter_app(data["login"]["user"], data["login"]["pass"])

    # 3. COMPRA MASIVA (Usando la lista del JSON)
    inventory = InventoryPage(page)
    lista_productos = data["compra_rapida"]

    for item in lista_productos:
        with allure.step(f"Añadiendo {item} desde el búnker de datos"):
            inventory.add_specific_product(item)
            
            # LÓGICA CONDICIONAL (Lo que te faltaba aprender)
            if item == "onesie":
                page.screenshot(path="foto_especial_onesie.png")

    # 4. VERIFICACIÓN
    expect(inventory.cart_icon).to_have_text(str(len(lista_productos)))