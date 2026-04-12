from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.product_locators import ProductLocators


class ProductPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/furn-9999-office-design-software-7?category=9')

    def get_breadcrumb(self):
        return self.get_text(ProductLocators.BREADCRUMB)

    def change_currency_to_eur(self):
        self.click(ProductLocators.PRICELIST_BTN)
        element = self.wait.until(EC.element_to_be_clickable(ProductLocators.EUR_PRICELIST))
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.staleness_of(element))

    def click_plus_multi(self, times):
        btn = self.find(ProductLocators.PLUS_BTN)
        for _ in range(times):
            btn.click()

    def add_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART_BTN)
        self.wait.until(lambda d: d.find_element(*ProductLocators.CART_COUNTER).text.strip() != "")
        self.wait.until(lambda d: int(d.find_element(*ProductLocators.CART_COUNTER).text) > 0)

    def go_to_cart_via_header(self):
        self.click(ProductLocators.HEADER_CART_ICON)
        self.wait.until(EC.url_contains("/shop/cart"))
        self.wait.until(EC.visibility_of_element_located(ProductLocators.CART_PRODUCTS_BLOCK))

    def remove_item_from_cart(self):
        btn = self.wait.until(EC.visibility_of_element_located(ProductLocators.REMOVE_ITEM_BTN))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.invisibility_of_element_located(ProductLocators.CART_PRODUCTS_BLOCK))

    def should_be_empty_cart(self):
        msg = self.wait.until(EC.visibility_of_element_located(ProductLocators.EMPTY_CART_MSG))
        assert "Your cart is empty!" in msg.text
        products_present = self.driver.find_elements(*ProductLocators.CART_PRODUCTS_BLOCK)
        assert len(products_present) == 0 or not products_present[0].is_displayed()

    def view_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(ProductLocators.VIEW_CART_BTN))
        self.driver.execute_script("arguments[0].click();", btn)

    def decrease_quantity_in_cart(self):
        input_element = self.find(ProductLocators.CART_QTY_INPUT)
        initial_val = input_element.get_attribute("value")
        minus_btn = self.find(ProductLocators.MINUS_BTN)
        self.driver.execute_script("arguments[0].click();", minus_btn)
        self.wait.until(lambda d: d.find_element(*ProductLocators.CART_QTY_INPUT).get_attribute("value") != initial_val)

    def wait_and_get_counter(self, expected_value):
        self.wait.until(EC.text_to_be_present_in_element(ProductLocators.CART_COUNTER, str(expected_value)))
        return self.get_text(ProductLocators.CART_COUNTER)

    def get_cart_input_value(self):
        return self.find(ProductLocators.CART_QTY_INPUT).get_attribute("value")
