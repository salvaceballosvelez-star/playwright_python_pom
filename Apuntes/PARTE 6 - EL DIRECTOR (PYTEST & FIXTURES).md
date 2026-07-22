🦾 SDET MASTER BIBLE: PARTE 6 - EL DIRECTOR (PYTEST & FIXTURES)
Esta sección explica cómo eliminar el código repetitivo y organizar las misiones para que el Ryzen 9 vuele.

🎭 1. ¿QUÉ ES PYTEST?
Es el motor que lanza los tests.

    Antes: Tenías que escribir with sync_playwright(), abrir el navegador, cerrarlo... (Mucha "grasa").
    Ahora: Pytest lo hace por ti. Tú solo escribes la lógica del test.

Regla de Oro de Naming:

    El archivo debe empezar por test_ (ej: test_login.py).
    La función debe empezar por test_ (ej: def test_compra_ok(page):).
    Si no pones el prefijo test_, Pytest ignorará el archivo.


🗝️ 2. LAS FIXTURES (El Mayordomo)
Una Fixture es una función que prepara el escenario antes de que empiece el test.

    Sintaxis: Se pone el "disfraz" @pytest.fixture encima de la función.
    Uso: Sirve para hacer el Login una sola vez y "prestárselo" a todos los tests.


⏳ 3. LA PALABRA MÁGICA: yield
Es el corazón del ciclo de vida. Significa "Pausa y Entrega".

    Lo que hay ANTES del yield: Es el Setup (Precalentamiento). Ej: Hacer el login.
    El yield: El Mayordomo te entrega el navegador y se queda esperando a que termines tu test.
    Lo que hay DESPUÉS del yield: Es el Teardown (Limpieza). Se ejecuta cuando el test termina (haya pasado o fallado).

🏰 4. LÓGICA RESIDENT EVIL (Encadenamiento)
Puedes usar una llave para conseguir la siguiente. Esto crea "puntos de guardado" en la web.

    Llave 1 (login_ready): Te deja en el Inventario.
    Llave 2 (backpack_in_cart): Pide la Llave 1, añade la mochila y te deja en el Carrito.
    Llave 3 (ready_to_pay): Pide la Llave 2, clica en Checkout y te deja en el Formulario.

¿Por qué es Senior esto? Porque si quieres testear el Formulario, no escribes el login. Solo pides la Llave 3 en el paréntesis de tu test y Pytest abre las 3 puertas por ti en milisegundos.

📄 5. EL ARCHIVO conftest.py
Es la Central de Llaves.

    Este archivo vive en la raíz del proyecto.
    Pytest lo lee automáticamente.
    Todas las Fixtures que pongas aquí estarán disponibles para TODOS tus tests sin tener que importarlas.


🧪 6. EJEMPLO DE TEST INYECTADO
Mira qué limpio queda un test cuando el Mayordomo hace el trabajo sucio:

# El test pide la llave 'backpack_in_cart'
def test_verificar_precio_carrito(backpack_in_cart):
    # 1. Instanciamos el manual (backpack_in_cart ya es el navegador)
    cart = CartPage(backpack_in_cart)
    
    # 2. El test empieza DIRECTAMENTE en el carrito
    expect(cart.item_price_label).to_have_text("$29.99")

💡 7. EL TRUCO DEL AUTOCOMPLETADO (: Page)
Pytest a veces "ciega" a VS Code. Para que el código salga en Amarillo y te sugiera comandos, usa el Type Hinting:

    def test_mision(login_ready: Page):
    Al poner : Page, VS Code sabe que login_ready es un navegador y te ayudará.