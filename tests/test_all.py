import pytest
from pages.login_page import LoginPage
from pages.contact_page import ContactPage
from pages.language_page import LanguagePage
from pages.filter_page import FilterPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("search_query, expect_results", [
    ("Hammer", True),
    ("Screw", True),
    ("Forge", False),
])
def test_search(tools, search_query, expect_results):
    filter_page = FilterPage(tools)
    count = filter_page.search(search_query)
    assert (count > 0) == expect_results

def test_login_logout(tools):
    login_page = LoginPage(tools)
    login_page.open_login()
    login_page.login("admin@practicesoftwaretesting.com", "welcome01")
    assert login_page.is_logged_in()
    login_page.logout()
    assert login_page.is_logged_out()

def test_contact_form(tools):
    contact_page = ContactPage(tools)
    contact_page.fill_contact_form('Test1', 'Test2', 'test@test.com', 'Return', 'I am a test message, I am a test message, I am a test message')
    assert tools.wait_for_selector("text=Thanks for your message!").is_visible()

def test_language(tools):
    language_page = LanguagePage(tools)
    lang_map = {
        "lang-de": "Anmelden",
        "lang-en": "Sign in",
        "lang-es": "Iniciar sesi\u00f3n",
        "lang-fr": "Connexion",
        "lang-nl": "Inloggen",
        "lang-tr": "Giri\u015f yap"
    }
    for code, expected_text in lang_map.items():
        assert language_page.change_language_and_verify(code, expected_text)

def test_buy(tools):
    checkout_page = CheckoutPage(tools)
    assert checkout_page.buy_product().is_visible()