🦾 SDET MASTER BIBLE: PARTE 1 - LA INFRAESTRUCTURA (EL TALLER)
Esta sección explica dónde vive cada cosa y por qué. Si el taller está desordenado, las piezas salen defectuosas.

📂 1. MAPA DE CARPETAS (La Jerarquía de Mando)
Todo debe ejecutarse desde la carpeta RAÍZ (playwright_python_pom).

📂 pages/ (Los Manuales de Instrucciones):
    Aquí creas un archivo .py por cada pantalla de la web (ej: login_page.py).
    Contenido: Solo "Carpintería" (Locators y Métodos).
    Regla de Oro: Prohibido usar expect aquí. Las páginas no juzgan, solo obedecen.

📂 tests/ (El Campo de Batalla):
    Aquí creas los archivos que empiezan por test_.
    Contenido: La estrategia. Llamas a las páginas y usas al Juez (expect).

📄 conftest.py (El Mayordomo / Puntos de Guardado):
    Es el archivo más importante. Aquí guardas las Fixtures (las llaves de Resident Evil).
    Sirve para que los tests empiecen directamente donde tú quieras (Login hecho, Carrito lleno, etc.).

📄 pytest.ini (La BIOS del Sistema):
    Archivo de configuración. Le dice a Pytest: "Oye, usa siempre Chrome, ve lento y busca los tests en la carpeta /tests".

⚙️ 2. EL CEREBRO: pytest.ini (Configuración Automática)
Para no tener que escribir comandos largos en la terminal, dejamos las órdenes grabadas aquí.

Contenido del archivo:

[pytest]
# addopts: Órdenes que se ejecutan SIEMPRE
# --headed: Abre el navegador para que lo veas (si lo quitas, es invisible/rápido)
# --slowmo 500: Espera medio segundo entre cada clic (para que no te ralles)
addopts = --headed --slowmo 500

# testpaths: Le dice a Pytest dónde están tus misiones
testpaths = tests

🗝️ 3. EL MAYORDOMO: conftest.py (Fixtures y Teletransporte)
Este archivo gestiona el "antes" y el "después" de cada test.

Conceptos clave para tontos:

@pytest.fixture: Es el "disfraz" que le pones a una función para que Pytest sepa que es una herramienta de preparación, no un test.

yield: Es la palabra mágica. Significa: "Hago todo lo de arriba (Login), te doy el mando (pausa), y cuando termines tu test, sigo con lo de abajo (Limpiar)".

Inyección: Si un test quiere empezar logueado, solo tiene que poner el nombre de la función del conftest en su paréntesis.

Ejemplo de "Llave Mansión" (Login):
@pytest.fixture
def login_ready(page):
    # 1. PREPARACIÓN (Setup)
    page.goto("https://www.saucedemo.com")
    # ... código de login ...
    
    # 2. ENTREGA DEL MANDO
    yield page 
    
    # 3. LIMPIEZA (Teardown)
    print("Test finalizado, cerrando sesión...")


# Instalar en otro ordenador que no trabajes normalmente 

🚀 TU LISTA DE "PUESTA A PUNTO" EN EL CURRO:

Para que no te vuelva a salir un error rojo en la oficina, asegúrate de haber lanzado estos 4 comandos en este PC (uno detrás de otro):
    El instalador de librerías: python -m pip install pytest-playwright
    El generador de HTML: python -m pip install pytest-html
    El conector de Allure: python -m pip install allure-pytest
    Los navegadores: python -m playwright install