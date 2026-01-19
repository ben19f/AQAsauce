from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open(self, url: str):
        self.page.goto(url)

    def login(self, username: str = "", password: str = ""):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_text(self) -> str:
        return self.page.text_content(self.error_message)
