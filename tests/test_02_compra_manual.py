# 1. EL ARSENAL COMPLETO
# Importamos TODOS los manuales de página porque este test va a pasar por todas las pantallas.
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverViewPage
# El Juez para validar cada paso
from playwright.sync_api import expect

# 2. INICIO DE LA MISIÓN
# Usamos 'page' a secas. Este test NO usa teletransportes (fixtures), lo hace todo a mano.
def test_comprar_pytest(page):

    # 3. CONTRATACIÓN DE ESPECIALISTAS
    # Creamos una variable por cada página. Todos comparten el mismo navegador (page).
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    overview = OverViewPage(page)

    # 4. FASE 1: EL ACCESO
    page.goto("https://www.saucedemo.com")
    login.enter_app("standard_user", "secret_sauce")
    # Verificamos que hemos entrado (Sanity Check)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 5. FASE 2: EL ALMACÉN
    # Añadimos la mochila y clicamos en el icono del carrito
    inventory.add_specific_product("backpack")
    inventory.go_to_cart()
    # Verificamos que el viaje al carrito ha funcionado
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    # 6. FASE 3: LA CESTA
    # Pulsamos el botón 'Checkout' para ir a poner nuestros datos
    cart.proceed_to_checkout()
    # Verificamos que estamos en la pantalla de 'Your Information'
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    # 7. FASE 4: EL FORMULARIO
    # Rellenamos nombre, apellido y código postal
    checkout.fill_shipping_info("Salvador", "ceballos", "21110")
    # Pulsamos continuar (si tu método fill_shipping_info no lo hace ya solo)
    # Verificamos que estamos en la pantalla de 'Overview' (Resumen)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # 8. FASE 5: EL PAGO FINAL
    # Pulsamos el botón 'Finish'
    overview.finish_shopping()
    # Verificamos que la URL final es la de 'Complete' (Éxito)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")