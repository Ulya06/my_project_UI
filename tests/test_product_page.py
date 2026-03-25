from pages.product_page import ProductPage


def test_add_to_cart_button_text(driver):
    page = ProductPage(driver)
    page.open_page()
    assert 'Add to cart' in page.get_add_button_text()


def test_breadcrumb_multimedia(driver):
    page = ProductPage(driver)
    page.open_page()
    assert 'Multimedia' in page.get_breadcrumb()


def test_quantity_input_default_value(driver):
    page = ProductPage(driver)
    page.open_page()
    assert page.get_quantity() == 1


def test_product_image_visible(driver):
    page = ProductPage(driver)
    page.open_page()
    assert page.is_image_visible()
