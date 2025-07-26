class ContactPage:
    def __init__(self, page):
        self.page = page

    def fill_contact_form(self, first_name, last_name, email, subject, message):
        self.page.get_by_text('Contact').click()
        self.page.fill('input#first_name', first_name)
        self.page.fill('input#last_name', last_name)
        self.page.fill('input#email', email)
        self.page.select_option('#subject', value=subject)
        self.page.fill('textarea#message', message)
        self.page.get_by_role('button', name='Send').click()