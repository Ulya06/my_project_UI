from pages.category_page import CategoryPage


def test_change_pricelist_to_eur(driver):
    page = CategoryPage(driver)
    page.open_page()
    page.change_currency_to_eur()
    assert '€' in page.get_price_text()


def test_products_are_displayed(driver):
    page = CategoryPage(driver)
    page.open_page()
    assert page.get_products_count() > 0


def test_first_product_has_title(driver):
    page = CategoryPage(driver)
    page.open_page()
    assert page.get_first_product_name() != ''


def test_breadcrumb_contains_desks(driver):
    page = CategoryPage(driver)
    page.open_page()
    assert 'Desks' in page.get_breadcrumb()


def test_open_product_page(driver):
    page = CategoryPage(driver)
    page.open_page()
    name = page.get_first_product_name()
    page.open_first_product()
    assert name in driver.page_source
