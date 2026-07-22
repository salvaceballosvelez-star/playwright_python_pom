from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators para productos
        self.backpack_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self.tshirt_btn = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.remove_tshirt_btn = page.locator("[data-test='remove-sauce-labs-bolt-t-shirt']")
        
        # Locators de navegación y UI
        self.cart_icon = page.locator(".shopping_cart_link")
        self.menu_btn = page.locator("#react-burger-menu-btn")
        self.logout_btn = page.locator("#logout_sidebar_link")
        self.sort_dropdown = page.locator("[data-test='product_sort_container']")
        
        # Locator para leer nombres (Vital para el test de ordenación)
        self.item_names = page.locator(".inventory_item_name")

    # --- MÉTODOS DE ACCIÓN ---
    def add_backpack(self): 
        self.backpack_btn.click()
        

    def add_tshirt(self): 
        self.tshirt_btn.click()

    def add_specific_product(self, product_name):
        dynamic_selector = f"[data-test='add-to-cart-sauce-labs-{product_name}']"
        self.page.locator(dynamic_selector).click()
    
    def remove_tshirt(self): 
        self.remove_tshirt_btn.click()

    def go_to_cart(self): 
        self.cart_icon.click()

    def go_to_burguer_btn(self): 
        self.menu_btn.click()

    def go_to_logout(self): 
        self.logout_btn.click()

    def filter_by_price_low_to_high(self):
        # Selecciona el valor 'lohi' que significa Low to High
        self.sort_dropdown.select_option("lohi")