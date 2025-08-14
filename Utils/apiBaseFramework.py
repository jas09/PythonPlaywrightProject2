from playwright.sync_api import Playwright
import os

ordersPayload = {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"},{"country":"India","productOrderedId":"67a8df1ac0d3e6622a297ccb"},{"country":"India","productOrderedId":"67a8df56c0d3e6622a297ccd"}]}
folder_path = r"D:\Python_Playwright_Project2\Screenshots"
class APIUtils:

    def getToken(self,playwright: Playwright, user_credentials):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                 data={"userEmail": user_credentials["userEmail"],
                                       "userPassword": user_credentials["userPassword"]})
        print("Status:", response.status)
        print("Body:", response.text())
        assert response.ok
        responseBody = response.json()
        return responseBody["token"]

    def maintain_screenshot_limit(self,folder_path, limit=20):
        # Get all .png files sorted by creation time (oldest first)
        screenshots = sorted(
            [f for f in os.listdir(folder_path) if f.endswith('.png')],
             key=lambda x: os.path.getctime(os.path.join(folder_path, x))
        )
        # Remove oldest files if count exceeds limit
        while len(screenshots) > limit:
            oldest = screenshots.pop(0)
            os.remove(os.path.join(folder_path, oldest))
            print(f"Removed old screenshot: {oldest}")

    def createOrder(self,playwright : Playwright,user_credentials):
        token = self.getToken(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"authorization": token,
                                          "content-type": "application/json"})
        print(response.json())
        response_body = response.json()
        ordersList = response_body["orders"]
        return ordersList
