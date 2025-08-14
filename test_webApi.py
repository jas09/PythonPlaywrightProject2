import json

import pytest
from playwright.sync_api import Playwright, expect

from Utils.apiBase import APIUtils

#Json file -> util -> access into Test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright : Playwright, user_credentials):
    chromeBrowser = playwright.chromium.launch(headless=False)
    context = chromeBrowser.new_context()
    page = context.new_page()

    #create order -> order ID
    apiUtils = APIUtils()
    ordersList = apiUtils.createOrder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("azharulla.mohammed1701@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("1234567")
    page.locator("#login").click()

    #orders History page -> order is present
    page.get_by_role("button", name="ORDERS").click()
    for order_id in ordersList:
        print(f"Opening order: {order_id}")
        row = page.locator("tr").filter(has_text=order_id)
        row.get_by_role("button", name="View").click()
        expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
        page.screenshot(path=f"Screenshots/order_{order_id}.png")
        page.get_by_role("button", name="ORDERS").click()
        print("Order Screenshot is saved")

    apiUtils.maintain_screenshot_limit('screenshots')
    context.close()



