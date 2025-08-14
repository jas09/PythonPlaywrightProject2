from playwright.sync_api import Page, expect


def test_uiValidationDynamicScript(page:Page):
    #Sauce Labs Fleece Jacket,Sauce Labs Onesie -> Verify 2 items showing the cart
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()
    Jacket = page.locator(".inventory_item").filter(has_text="Sauce Labs Fleece Jacket")
    Jacket.get_by_role("button").click()
    Onesie = page.locator(".inventory_item").filter(has_text="Sauce Labs Onesie")
    Onesie.get_by_role("button").click()
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(2)