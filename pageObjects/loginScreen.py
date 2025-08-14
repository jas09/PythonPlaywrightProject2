from pageObjects.dashBoardPage import DashboardPage


class LoginPage:

    def __init__(self,page):
        self.page = page


    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,Email,Password):
        self.page.get_by_placeholder("email@example.com").fill(Email)
        self.page.get_by_placeholder("enter your passsword").fill(Password)
        self.page.locator("#login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
