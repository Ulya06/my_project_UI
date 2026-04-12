import pytest


def test_breadcrumb_multimedia(product_page):
    assert 'Multimedia' in product_page.get_breadcrumb()

def test_quantity_adjustment_and_cart_sync(product_page):
    product_page.click_plus_multi(10)
    product_page.add_to_cart()
    product_page.view_cart()

    initial_qty = int(product_page.get_cart_input_value())
    product_page.decrease_quantity_in_cart()

    new_qty = int(product_page.get_cart_input_value())
    counter = int(product_page.wait_and_get_counter(new_qty))

    assert new_qty == initial_qty - 1
    assert counter == new_qty

def test_change_currency_and_remove_from_cart(product_page):
    product_page.change_currency_to_eur()
    product_page.click_plus_multi(2)
    product_page.add_to_cart()
    product_page.go_to_cart_via_header()
    product_page.remove_item_from_cart()
    product_page.should_be_empty_cart()
