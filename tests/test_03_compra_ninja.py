# 1. EL EQUIPO DE GALA
# Importamos 'allure' para que el reporte tenga colores y títulos.
import allure
# Importamos 'Page' para el autocompletado y 'expect' para que actúe el Juez.
from playwright.sync_api import Page, expect

# 2. CARÁTULA DEL REPORTE (Decoradores)
# Esto es lo que verá tu jefe en la web del informe.
@allure.title("Misión: Compra Express de Mochila") 
# Definimos que si este test falla, es una catástrofe (Nivel Crítico).
@allure.severity(allure.severity_level.CRITICAL) 

# 3. LA LLAVE MAESTRA
# Pedimos 'checkout_step_two'. Aparecemos mágicamente en la pantalla final.
def test_fast_delivery(checkout_step_two: Page):
    
    # 4. PASOS DOCUMENTADOS
    # 'with allure.step' agrupa las acciones en el reporte para que sea legible.
    with allure.step("Verificar que el mensaje de éxito es visible y correcto"):
        
        # Localizamos el cartel de "Thank you..."
        success_msg = checkout_step_two.locator("[data-test='complete-header']")
        
        # El Juez (expect) comprueba que el texto es el que prometió el negocio.
        # Si esto falla, Allure marcará este PASO concreto en ROJO.
        expect(success_msg).to_have_text("Thank you for your order!")
    
    # 5. EL GRITO DE VICTORIA
    # Este mensaje solo lo verás tú en la terminal si usas el comando '-s'.
    print("¡BRUTAL! Prueba terminada usando el teletransporte completo.")