class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def buy_product(self):
        self.page.locator('.card').first.click()
        self.page.get_by_text('Add to cart').click()
        self.page.locator('[data-test="nav-cart"]').click()
        self.page.get_by_role('button', name='Proceed to checkout').click()

        self.page.fill('input#email', 'admin@practicesoftwaretesting.com')
        self.page.fill('input#password', 'welcome01')
        self.page.get_by_role('button', name='Login').click()

        self.page.get_by_role('button', name='Proceed to checkout').click()
        self.page.wait_for_timeout(2000)
        self.page.fill('input#state', 'test')
        self.page.fill('input#postal_code', 'test')
        self.page.get_by_role('button', name='Proceed to checkout').click()
        self.page.select_option('#payment-method', value='Cash on Delivery')
        self.page.get_by_role('button', name='Confirm').click()

        return self.page.wait_for_selector('text=Payment was successful')