from playwright.sync_api import Page, Playwright

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

def test_playwrightShortCut(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()
    print(page.locator(".footer_copy").text_content())

def test_fireFoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox
    firefox = firefoxBrowser.launch(headless=True)
    page = firefox.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()
    #2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy
    text = page.locator(".footer_copy").text_content()
    words = text.split("|")
    actual_result = words[1].strip()
    assert actual_result == "Privacy Policy"


