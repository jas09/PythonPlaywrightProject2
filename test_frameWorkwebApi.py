import json

import pytest
from playwright.sync_api import Playwright

from Utils.apiBaseFramework import APIUtils
from pageObjects.loginScreen import LoginPage

#Json file -> util -> access into Test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']
#def load_credentials():
    #with open('data/credentials.json') as f:
        #test_data = json.load(f)
        #return test_data['user_credentials']

@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright : Playwright,browserInstance, user_credentials):
    Email = user_credentials["userEmail"]
    Password = user_credentials["userPassword"]

    #create order -> order ID
    apiUtils = APIUtils()
    ordersList = apiUtils.createOrder(playwright,user_credentials)

    #login
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(Email,Password)
    #orders History page -> order is present
    orderHistoryPage = dashboardPage.selectOrdersNavigationLink()
    for order_id in ordersList:
        print(f"Opening order: {order_id}")
        orderDetailsPage = orderHistoryPage.selectOrder(order_id)
        orderDetailsPage.verifyOrderMessage()
        browserInstance.screenshot(path=f"Screenshots/order_{order_id}.png")
        dashboardPage.selectOrdersNavigationLink()
        print("Order Screenshot is saved")

    apiUtils.maintain_screenshot_limit('screenshots')


