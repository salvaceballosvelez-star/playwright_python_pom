# 1. LAS HERRAMIENTAS
from pages.cart_page import CartPage
from playwright.sync_api import expect

# 2. EL REFUGIO (FIXTURE)
# Pedimos 'add_backpack'. El test empieza DIRECTAMENTE en el carrito con la mochila dentro.
# Pytest ha hecho el login y ha añadido el producto por nosotros.
def test_clean_cart(add_backpack):
    
    # 3. LLAMAMOS AL ESPECIALISTA DEL CARRITO
    cart = CartPage(add_backpack)

    # 4. LA ORDEN DE LIMPIEZA (ENCAPSULAMIENTO)
    # Fíjate: ¡Aquí no hay bucles 'for'! 
    # El bucle está escondido dentro del manual 'CartPage.py'.
    # El test solo da la orden de alto nivel: "Vacíate".
    cart.all_remove_items()

    # 5. EL JUEZ (VERIFICACIÓN)
    # Comprobamos que el nombre del producto YA NO SE VE en pantalla.
    # '.not_to_be_visible()' es el comando para asegurar que algo ha desaparecido.
    expect(cart.item_name_label).not_to_be_visible()
    
    # 6. EL ÉXITO
    print("¡GREEN! El carro se ha vaciado correctamente usando lógica industrial.")