from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_sorting_flow():
    with sync_playwright() as p:
        # headless=False para que veas el éxito en directo
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        inventory = InventoryPage(page)

        page.goto("https://www.saucedemo.com")

        # 1. Login
        login.enter_app("standard_user", "secret_sauce")
        
        # 2. Ordenar (Acción directa, no hace falta abrir el menú)
        inventory.filter_by_price_low_to_high()
        
        # 3. Validar: El primer nombre de la lista debe ser el pijama (Onesie)
        expect(inventory.item_names.first).to_have_text("Sauce Labs Onesie")

        print("¡LOGRADO! El filtrado funciona y el Onesie está en primera posición.")
        
        # 4. Limpieza
        browser.close()

if __name__ == "__main__":
    test_sorting_flow()