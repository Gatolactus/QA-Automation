class LoginPage:
    def __init__(self, page):
        self.page = page
        self.sign_in_link = page.get_by_text('Sign in')
        self.email_input = page.locator('input#email')
        self.password_input = page.locator('input#password')
        self.login_button = page.get_by_role('button', name='Login')
        self.menu_button = page.locator("a#menu")
        self.sign_out_link = page.locator("a[data-test='nav-sign-out']")

    def open_login(self):
        self.sign_in_link.click()

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.menu_button.hover()
        self.page.wait_for_selector("a[data-test='nav-sign-out']", state="visible")
        self.sign_out_link.click()

    def is_logged_out(self):
        return self.sign_in_link.is_visible()

    def is_logged_in(self):
        self.menu_button.click()
        return self.sign_out_link.is_visible()