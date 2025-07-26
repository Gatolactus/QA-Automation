import pytest 

@pytest.fixture
def tools(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    yield page
    context.close()