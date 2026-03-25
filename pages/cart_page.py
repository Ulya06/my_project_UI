from pages.base_page import BasePage
from pages.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/cart')

    def get_empty_cart_text(self):
        return self.get_text(CartLocators.EMPTY_CART)

    def get_header(self):
        return self.get_text(CartLocators.HEADER)

    def click_contact(self):
        self.click(CartLocators.CONTACT_BTN)

    def open_search(self):
        self.click(CartLocators.SEARCH_BTN)

    def get_warning_text(self):
        return self.get_text(CartLocators.WARNING)
