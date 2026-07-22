🦾 SDET MASTER BIBLE: PARTE 10 - GUÍA DE ENSAMBLAJE (CÓMO CREAR UN TEST)
Esta sección es el "paso a paso" universal. No importa si el test es de login o de comprar un tanque: el orden de los ladrillos siempre es el mismo.
🏗️ 1. LA ANATOMÍA DE UN ARCHIVO DE TEST
Un archivo de test profesional tiene 4 bloques sagrados. Si falta uno, el Ryzen 9 no sabrá qué hacer.
BLOQUE A: Las Importaciones (Traer a los actores)
Arriba del todo, traes los manuales de las páginas que vas a usar y al Juez.

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect, Page

BLOQUE B: La Definición (El nombre de la misión)
La función TIENE que empezar por test_. En el paréntesis pides la "llave" (fixture) que necesites del conftest.py.

def test_mi_mision_nueva(login_ready: Page): # Pedimos la llave de Login

BLOQUE C: La Instanciación (Darle pilas a los manuales)
Creas los objetos de las páginas pasándoles el navegador que has pedido en el paréntesis. Es como conectar el cable a la impresora.

inventory = InventoryPage(login_ready)
    cart = CartPage(login_ready)

BLOQUE D: La Acción y el Juez (Jugar la partida)
Das las órdenes y compruebas el resultado final.

inventory.add_backpack()
    inventory.go_to_cart()
    expect(login_ready).to_have_url("https://www.saucedemo.com/cart.html")


🧭 2. ¿DÓNDE MIRAR SEGÚN LO QUE NECESITES?
Si quieres...	Mira en tus apuntes...
Saber qué botón pulsar	PARTE 2 (Métodos de la Page)
Saber cómo encontrar un ID	PARTE 4 (Selectores)
Saber cómo validar un texto	PARTE 3 (Aserciones)
Saber qué llave (fixture) usar	PARTE 6 (Fixtures en conftest.py)
💡 3. EL FLUJO DE TRABAJO DEL SENIOR (Tu nueva rutina)
¿Qué quiero probar? (Ej: Que el mensaje de error de login sale en rojo).
¿Tengo los botones mapeados? Si no, voy a la Página y los añado (Parte 2).
¿Desde dónde quiero empezar? Si quiero empezar desde la web vacía, pido page. Si quiero empezar logueado, pido login_ready (Parte 6).
Escribo el Test siguiendo el esquema del Bloque A, B, C y D.
Lanzó el comando en la terminal (Parte 8).