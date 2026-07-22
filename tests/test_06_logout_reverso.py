# 1. TRAEMOS LOS MANUALES Y AL JUEZ
from pages.overview_page import OverViewPage
# Importamos 'Page' para el autocompletado y 'expect' para validar
from playwright.sync_api import Page, expect

# 2. LA MISIÓN NINJA
# Pedimos la 'Llave Maestra' (checkout_step_two).
# Este test empieza DIRECTAMENTE en la pantalla final de "Gracias por su compra".
# Pytest ha hecho todo el camino (Login, Carro, Pago) por nosotros en milisegundos.
def test_ninja(checkout_step_two: Page):
    
    # 3. VERIFICACIÓN DE ENTRADA
    # Antes de escapar, comprobamos que realmente estamos en la meta.
    success_msg = checkout_step_two.locator("[data-test='complete-header']")
    expect(success_msg).to_have_text("Thank you for your order!")

    # 4. CONTRATAMOS AL ESPECIALISTA
    # Creamos el objeto 'overview'. Le pasamos el navegador que ya está en la meta.
    overview = OverViewPage(checkout_step_two)

    # 5. LA ACCIÓN DE ESCAPE (MÉTODO COMPLEJO)
    # Llamamos a la habilidad 'logout'. 
    # Recuerda que este método hace DOS cosas: abre el menú y clica en Logout.
    overview.logout() 

    # 6. EL JUEZ FINAL (LA PRUEBA DEL CRIMEN)
    # Verificamos que el navegador nos ha expulsado a la página de inicio.
    # ¡OJO! La barrita final '/' es sagrada, sin ella el test falla.
    expect(checkout_step_two).to_have_url("https://www.saucedemo.com/")
    
    # 7. EL GRITO DE VICTORIA
    print("¡BRUTAL! El Ninja ha comprado y ha escapado sin dejar rastro.")