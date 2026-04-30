from pages.base_page import BasePage
from pages.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/cart')

    def open_desks_in_new_tab(self):
        self.hover(CartLocators.CATEGORIES_MENU)
        self.open_link_with_ctrl(CartLocators.DESKS_LINK)
        self.switch_to_tab(1)

    def open_furn_in_new_tab(self):
        self.hover(CartLocators.CATEGORIES_MENU)
        self.open_link_with_ctrl(CartLocators.FURN_LINK)
        self.switch_to_tab(1)

    def close_tab_and_return(self):
        self.driver.close()
        self.switch_to_tab(0)

    def verify_url_contains(self, word):
        self.wait.until(lambda d: word in d.current_url)
        assert word in self.driver.current_url

    def should_be_correct_header(self, expected_text):
        actual_text = self.get_text(CartLocators.HEADER)
        assert expected_text in actual_text

    def should_be_empty_cart_message(self, expected_text):
        actual_text = self.driver.page_source
        assert expected_text in actual_text

    def click_contact_us(self):
        self.click(CartLocators.CONTACT_BTN)

    def click_submit(self):
        btn = self.find(CartLocators.SUBMIT_BTN)
        self.driver.execute_script("arguments[0].click();", btn)

    def should_be_validation_error(self, expected_text):
        actual_text = self.get_text(CartLocators.FORM_RESULT).strip()
        assert expected_text in actual_text

    def open_search(self):
        self.click(CartLocators.SEARCH_BTN)

    def should_be_warning_text(self, expected_text):
        actual_text = self.get_text(CartLocators.WARNING)
        assert expected_text in actual_text
