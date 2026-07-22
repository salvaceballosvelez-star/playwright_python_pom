from playwright.sync_api import sync_playwright, expect

def test_plane_of_scape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo= 1000)
        page = browser.new_page()

        from pages.login_page import LoginPage
        from pages.inventory_page import InventoryPage
        
        login = LoginPage(page)
        Inventory = InventoryPage(page)

        page.goto("https://www.saucedemo.com")

        login.enter_app("standard_user", "secret_sauce")
        Inventory.go_to_burguer_btn()
        Inventory.go_to_logout()

        browser.close()

if __name__ == "__main__":
    test_plane_of_scape()
    
        