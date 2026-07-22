#Traemos la herramientas (login y playright)
from pages.login_page import LoginPage
from playwright.sync_api import expect
import allure

#Definimos el test, debe empezar por test
#para Pytest y poner page para autocompletar
@allure.title("Misión 08: Bloqueo por Credenciales Incorrectas")
@allure.severity(allure.severity_level.NORMAL)

def test_login_error(page):
# Creamos el objeto 'login'. Le pasamos el navegador (page) para que sepa dónde actuar.
    login = LoginPage(page)
   
# 4. PASOS DE LA MISIÓN
# Vamos a la web
    page.goto("https://www.saucedemo.com/")

    with allure.step("Introducir credenciales erroneas"):
        login.enter_app("standard_user", "password_falsa")

    with allure.step("Verificar mensaje de error en pantalla"):
        expect(login.error_message_text).to_contain_text("Epic sadface: Username and password do not match any user in this service")

    print("LOG: Mensaje de error validado con exito")
    