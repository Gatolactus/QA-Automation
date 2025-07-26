class LanguagePage:
    def __init__(self, page):
        self.page = page

    def change_language_and_verify(self, lang_code, expected_text):
        self.page.locator('#language').click()
        self.page.wait_for_selector(f'[data-test="{lang_code}"]')
        self.page.locator(f'[data-test="{lang_code}"]').click()
        return self.page.locator('[data-test="nav-sign-in"]').is_visible()