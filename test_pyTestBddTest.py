import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from Utils.apiBaseFramework import APIUtils
from pageObjects.loginScreen import LoginPage

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username,password,shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    apiUtils = APIUtils()
    ordersList = apiUtils.createOrder(playwright, user_credentials)
    shared_data['orders_List'] = ordersList

@given('user is on landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username,password,shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboard_page'] = dashboardPage

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_page']
    orderHistoryPage = dashboardPage.selectOrdersNavigationLink()
    shared_data['orderHistory_page'] = orderHistoryPage

@then('select the orderId & verify order message is successfully delivered')
def select_order_id(shared_data,browserInstance):
    orderHistoryPage = shared_data['orderHistory_page']
    api_utils = APIUtils()
    ordersList = shared_data['orders_List']
    dashboardPage = shared_data['dashboard_page']
    for order_id in ordersList:
        print(f"Opening order: {order_id}")
        orderDetailsPage = orderHistoryPage.selectOrder(order_id)
        orderDetailsPage.verifyOrderMessage()
        browserInstance.screenshot(path=f"Screenshots/order_{order_id}.png")
        dashboardPage.selectOrdersNavigationLink()
        print("Order Screenshot is saved")
        api_utils.maintain_screenshot_limit('screenshots')

