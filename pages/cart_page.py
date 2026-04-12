from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/cart')

    def should_be_correct_header(self, expected_text):
        actual_text = self.get_text(CartLocators.HEADER)
        assert expected_text in actual_text

    def should_be_empty_cart_message(self, expected_text):
        actual_text = self.get_text(CartLocators.EMPTY_CART)
        assert expected_text in actual_text

    def hover_categories(self):
        menu = self.find(CartLocators.CATEGORIES_MENU)
        ActionChains(self.driver).move_to_element(menu).perform()

    def open_link_with_ctrl(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        link = element.get_attribute('href')
        self.driver.execute_script(f'window.open("{link}", "_blank");')

    def switch_to_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def click_contact_us(self):
        self.click(CartLocators.CONTACT_BTN)

    def click_submit(self):
        btn = self.find(CartLocators.SUBMIT_BTN)
        self.driver.execute_script("arguments[0].click();", btn)

    def should_be_validation_error(self, expected_text):
        self.wait.until(EC.text_to_be_present_in_element(CartLocators.FORM_RESULT, expected_text))
        actual_text = self.get_text(CartLocators.FORM_RESULT)
        assert expected_text in actual_text

    def get_empty_cart_text(self):
        return self.get_text(CartLocators.EMPTY_CART)

    def click_contact(self):
        self.click(CartLocators.CONTACT_BTN)

    def open_search(self):
        self.click(CartLocators.SEARCH_BTN)

    def get_warning_text(self):
        return self.get_text(CartLocators.WARNING)
