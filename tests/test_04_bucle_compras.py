# 1. LAS HERRAMIENTAS
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

# 2. EL REFUGIO (FIXTURE)
# Pedimos 'login_ready'. El test empieza ya dentro de la tienda.
def test_massive_cart(login_ready):
    
    # 3. EL INVENTARIO DE LA MISIÓN (LA LISTA)
    # En lugar de escribir 4 líneas, creamos una lista con los nombres técnicos.
    # Es como decirle al Master: "Estos son los 4 monstruos que voy a invocar".
    items_to_buy = ["backpack", "bike-light", "bolt-t-shirt", "onesie"]
    
    # 4. LLAMAMOS AL ESPECIALISTA
    inventory = InventoryPage(login_ready)

    # 5. EL BUCLE 'FOR' (LA CADENA DE MONTAJE)
    # Esto se lee: "Por cada 'item' que haya en la caja 'items_to_buy'..."
    for item in items_to_buy:
        
        # 6. LA ACCIÓN DINÁMICA
        # Usamos la habilidad 'add_specific_product'. 
        # En cada vuelta del bucle, la máquina cambia el nombre del producto sola.
        # Vuelta 1: backpack | Vuelta 2: bike-light... etc.
        inventory.add_specific_product(item)
        
        # 7. EL CHIVATO (LOG)
        # Imprimimos en la consola para saber que el robot no se ha quedado "atontado".
        print(f"DEBUG: Añadiendo {item} al carrito")

    # 8. EL JUEZ FINAL (FUERA DEL BUCLE)
    # ¡OJO! El juez solo mira cuando la fábrica ha terminado de procesar toda la lista.
    # Miramos el icono del carrito y verificamos que el numerito es un "4".
    expect(inventory.cart_icon).to_have_text("4")