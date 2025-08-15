from playwright.sync_api import Playwright, expect

from Utils.apiBase import APIUtils

#Code is having error, need to work on it
def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    chromeBrowser = playwright.chromium.launch(headless=True)
    context = chromeBrowser.new_context()
    context.add_init_script(f"""
            // Store token in localStorage
            window.localStorage.setItem('token', '{getToken}');

            // Or in sessionStorage
            // window.sessionStorage.setItem('token', '{getToken}');
        """)
    #context.add_init_script(f""""localStorage.setItem('token','{getToken}')""")
    page = context.new_page()
    #Script to inject token in session local storage
    #page.add_init_script(f""""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
