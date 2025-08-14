from playwright.sync_api import Page

fakePayLoadResponse = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(json= fakePayLoadResponse)


def test_interceptNetwork(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("azharulla.mohammed1701@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("1234567")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)