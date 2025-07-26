class FilterPage:
    def __init__(self, page):
        self.page = page

    def filter_by_category(self, categories):
        for name in categories:
            self.page.locator(f'label:has-text("{name}") >> input[type="checkbox"]').check()

    def search(self, query):
        self.page.fill('input[data-test="search-query"]', query)
        self.page.get_by_role('button', name='Search').click()
        self.page.wait_for_selector('div[data-test="search_completed"]')
        return self.page.locator('div[data-test="search_completed"] .card').count()