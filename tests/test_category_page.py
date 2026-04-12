import pytest
from pages.category_page import CategoryPage


def test_change_pricelist_to_eur(driver):
    page = CategoryPage(driver)
    page.open_page()
    page.change_currency_to_eur()
    page.should_all_prices_be_in_eur()

def test_open_product_page(category_page):
    name = category_page.get_first_product_name()
    category_page.open_first_product()
    assert name in category_page.driver.page_source

def test_filter_list_and_add_to_cart(category_page):
    category_page.switch_to_list_view()
    category_page.select_steel_filter()
    category_page.click_cart_icon()
    category_page.proceed_to_checkout()
    category_page.should_be_on_cart_page()
    category_page.verify_product_in_cart(
        "Customizable Desk (Steel, White)",
        "160x80cm, with large legs."
    )
