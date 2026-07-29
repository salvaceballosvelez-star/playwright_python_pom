import pytest
import allure
import logging
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverViewPage

# 1. CONFIGURACIÓN DE LOGS (Nivel José Rodríguez)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# --- FIXTURES: LAS LLAVES DE LA MANSIÓN ---

@pytest.fixture
def login_ready(page):
    login = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    login.enter_app("standard_user", "secret_sauce")
    yield page 

@pytest.fixture
def add_backpack(login_ready):
    inventory = InventoryPage(login_ready)
    inventory.add_backpack()
    inventory.go_to_cart()
    yield login_ready

@pytest.fixture
def ready_to_checkout(add_backpack):
    cart = CartPage(add_backpack)
    cart.proceed_to_checkout()
    yield add_backpack   

@pytest.fixture
def checkout_step_one(ready_to_checkout):
    checkout = CheckoutPage(ready_to_checkout)
    checkout.fill_shipping_info("Salvador", "Ceballos", "21110")
    yield ready_to_checkout

@pytest.fixture
def checkout_step_two(checkout_step_one):
    overview = OverViewPage(checkout_step_one)
    overview.finish_shopping()
    yield checkout_step_one

# --- EL CHIVATO: FOTOS AUTOMÁTICAS EN FALLO ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        for arg in item.funcargs.values():
            if isinstance(arg, Page):
                allure.attach(
                    arg.screenshot(),
                    name="📸_EVIDENCIA_DEL_ERROR",
                    attachment_type=allure.attachment_type.PNG
                )
                break