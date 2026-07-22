from playwright.sync_api import Page

class CheckoutPage: # Nombre más descriptivo
    def __init__(self, page: Page):
        self.page = page # CORREGIDO: minúscula
        
        # --- INPUTS (Datos del cliente) ---
        self.first_name_field = page.locator("[data-test='firstName']") # data-test en minúscula
        self.last_name_field = page.locator("[data-test='lastName']")
        self.postal_code_field = page.locator("[data-test='postalCode']")
        
        # --- BOTONES DE ACCIÓN ---
        self.continue_btn = page.locator("[data-test='continue']")
        self.cancel_btn = page.locator("[data-test='cancel']")
        
        # --- TEXTOS DE VERIFICACIÓN ---
        self.title_txt = page.locator("[data-test='title']")

    # --- FALTA EL MÉTODO DE ACCIÓN ---
    def fill_shipping_info(self, first_name, last_name, zip_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(zip_code)
        self.continue_btn.click()

    def  click_cancel_(self):
        self.cancel_btn.click()
