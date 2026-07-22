import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverViewPage
import logging

# Configuración del formato de los mensajes
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Nivel 1 
@pytest.fixture
def login_ready(page):
    login = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    login.enter_app("standard_user", "secret_sauce")
    yield page 


# Nivel 2
@pytest.fixture
def add_backpack(login_ready):
    inventory = InventoryPage(login_ready)
    inventory.add_backpack()
    inventory.go_to_cart()
    yield login_ready

# Nivel 3
@pytest.fixture
def ready_to_checkout(add_backpack):
    cart = CartPage(add_backpack)
    cart.proceed_to_checkout()
    yield add_backpack   

# Nivel 4
@pytest.fixture
def checkout_step_one(ready_to_checkout):
    checkout = CheckoutPage(ready_to_checkout)
    checkout.fill_shipping_info("Salvador", "Ceballos", "21110")
    yield ready_to_checkout

# Nivel 5
@pytest.fixture
def checkout_step_two(checkout_step_one):
    overview = OverViewPage(checkout_step_one)
    overview.finish_shopping()
    yield checkout_step_one



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Este código vigila cada test que se ejecuta
    outcome = yield
    report = outcome.get_result()
    
    # SI EL TEST FALLA (y estamos en la fase de llamada):
    if report.when == "call" and report.failed:
        # Intentamos pillar el navegador de cualquier fixture que estemos usando
        page = item.funcargs.get("page") or item.funcargs.get("login_ready") or item.funcargs.get("checkout_step_two")
        
        if page:
            # SACAMOS LA FOTO Y LA PINCHAMOS EN EL REPORTE
            allure.attach(
                page.screenshot(),
                name="📸 FOTO_DEL_ERROR",
                attachment_type=allure.attachment_type.PNG
            )