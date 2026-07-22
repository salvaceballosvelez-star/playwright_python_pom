from playwright.sync_api import Page

class OverViewPage:
    def __init__(self, page: Page):
        self.page = page
        # CORREGIDO: Añadido el '=' que faltaba
        self.cancel_btn = page.locator("[data-test='cancel']")
        self.finish_btn = page.locator("[data-test='finish']") 
        self.total_price_label = page.locator("[data-test='total-label']")
        self.burguer_btn = page.locator("#react-burger-menu-btn")
        self.logout_btn = page.locator("#logout_sidebar_link")
    
    def cancel_shopping(self):
        self.cancel_btn.click()

    def finish_shopping(self):
        self.finish_btn.click()

    def logout(self):
        self.burguer_btn.click()
        self.logout_btn.click()


    def get_total_price(self):
        return self.total_price_label.inner_text()
    
    
