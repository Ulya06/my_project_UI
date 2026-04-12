import pytest
from pages.locators.cart_locators import CartLocators


def test_cart_header_and_empty_state(cart_page):
    cart_page.should_be_correct_header("Order overview")
    cart_page.should_be_empty_cart_message("Your cart is empty!")

def test_categories_tabs_navigation(cart_page):
    cart_page.hover_categories()
    cart_page.open_link_with_ctrl(CartLocators.DESKS_LINK)
    cart_page.switch_to_tab(1)
    assert "desks" in cart_page.driver.current_url
    cart_page.driver.close()
    cart_page.switch_to_tab(0)

    cart_page.hover_categories()
    cart_page.open_link_with_ctrl(CartLocators.FURN_LINK)
    cart_page.switch_to_tab(1)
    assert "furnitures" in cart_page.driver.current_url
    cart_page.driver.close()
    cart_page.switch_to_tab(0)
    cart_page.should_be_correct_header("Order overview")

def test_contact_us_validation(cart_page):
    cart_page.click_contact_us()
    cart_page.click_submit()
    cart_page.should_be_validation_error("Please fill in the form correctly.")
