from pages.cart_page import CartPage


def test_empty(driver):
    page = CartPage(driver)
    page.open_page()
    assert 'empty' in page.get_empty_cart_text().lower()


def test_h3(driver):
    page = CartPage(driver)
    page.open_page()
    assert page.get_header() == 'Order overview'


def test_contact_us(driver):
    page = CartPage(driver)
    page.open_page()
    page.click_contact()
    assert 'contact us' in driver.page_source.lower()
