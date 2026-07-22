from playwright.sync_api import Page

class CartPage:
    def __init__(self, page : Page):
        self.page = page
        # Mantenemos TODO tu inventario intacto
        self.item_price_label = page.locator("[data-test='inventory-item-price']")
        self.item_name_label = page.locator("[data-test='inventory-item-name']")
        self.item_descriptio_label = page.locator("[data-test='inventory-item-desc']")
        self.continue_btn = page.locator("[data-test='continue-shopping']")
        self.checkout_btn = page.locator ("[data-test='checkout']")
        self.remove_btn = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.all_remove_btns = page.locator(".cart_button")
    
    def proceed_to_checkout(self):
        self.checkout_btn.click()

    def remove_item(self):
        self.remove_btn.click()

    
    def all_remove_items(self):
        lista_botones = self.all_remove_btns.all()

        for boton in lista_botones:
            boton.click()

    