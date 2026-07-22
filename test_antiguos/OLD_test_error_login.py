from playwright.sync_api import sync_playwright , expect

from pages.login_page import LoginPage

def test_error_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False, slow_mo= 1000)
        page = browser.new_page()

        login = LoginPage(page)
    
        page.goto("https://www.saucedemo.com")
        login.enter_app("locked_out_user", "secret_sauce")
        expect(login.error_message_text).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

        print("Test error verificado correctamente")
        browser.close()


if __name__ == "__main__":
    test_error_login()