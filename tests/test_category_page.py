import pytest


def test_change_pricelist_to_eur(category_page):
    category_page.change_currency_to_eur()
    category_page.should_all_prices_be_in_eur()

def test_open_product_page(category_page):
    category_page.verify_product_name_in_source("Customizable Desk")
    category_page.open_first_product()
