# 1. TRAEMOS LAS HERRAMIENTAS
# Traemos el 'Manual de Instrucciones' del Login (LoginPage)
from pages.login_page import LoginPage
# Traemos al 'Juez' (expect) para que diga si el test pasa o falla
from playwright.sync_api import expect

# 2. DEFINIMOS LA MISIÓN
# 'test_' al principio es OBLIGATORIO para que Pytest lo encuentre.
# '(page)' es la llave mágica: Pytest nos regala el navegador ya abierto.
def test_login_standard(page):
    
    # 3. LLAMAMOS AL ESPECIALISTA
    # Creamos el objeto 'login'. Le pasamos el navegador (page) para que sepa dónde actuar.
    login = LoginPage(page)

    # 4. PASOS DE LA MISIÓN
    # Vamos a la web
    page.goto("https://www.saucedemo.com")
    
    # Usamos la habilidad 'enter_app' del manual. Le damos el usuario y la contraseña.
    login.enter_app("standard_user", "secret_sauce")

    # 5. EL VERDICTO DEL JUEZ
    # El Juez mira la dirección del navegador (URL).
    # Si la dirección es 'inventory.html', el test se pone en VERDE.
    # Si no, el test se pone en ROJO y se para.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")