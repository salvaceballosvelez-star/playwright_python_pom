# 1. TRAEMOS LAS HERRAMIENTAS
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page, expect

# 2. LA MISIÓN: Sacar fotos de la página mientras compramos
def test_paparazzi_full_context(login_ready: Page):
    
    # 3. CARGAMOS AL ESPECIALISTA
    inventory = InventoryPage(login_ready)

    # 4. LA LISTA DE LA COMPRA
    items = ["backpack", "bike-light", "onesie"]

    # 5. EL BUCLE INDUSTRIAL (Acción + Foto)
    for item in items:
        
        # --- PASO A: ACCIÓN ---
        # Añadimos el producto usando tu método dinámico
        inventory.add_specific_product(item)

        # --- PASO B: EVIDENCIA ---
        # Sacamos foto de TODA LA PÁGINA (login_ready es el navegador)
        # Así veremos cómo el numerito del carrito va subiendo
        login_ready.screenshot(path=f"evidencia_compra_{item}.png")
        
        print(f"EVIDENCIA GUARDADA: {item} añadido al carrito.")

    # 6. EL JUEZ FINAL
    # Verificamos que, tras el bucle, el carrito marca "3"
    expect(inventory.cart_icon).to_have_text("3")

    print("\n[MISION CUMPLIDA] Revisa tus archivos .png para ver el progreso.")
