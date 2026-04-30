import re
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.product_locators import ProductLocators


class ProductPage(BasePage):
    def open_page(self):
        self.open(self.base_url + 'shop/furn-9999-office-design-software-7?category=9')

    def check_breadcrumb(self, expected_text):
        actual_text = self.get_text(ProductLocators.BREADCRUMB)
        assert expected_text in actual_text

    def change_currency_to_eur(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        btn = self.find(ProductLocators.PRICELIST_BTN)
        self.driver.execute_script("arguments[0].click();", btn)

        element = self.wait.until(EC.element_to_be_clickable(ProductLocators.EUR_PRICELIST))
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.staleness_of(element))

    def click_plus_multi(self, times):
        btn = self.find(ProductLocators.PLUS_BTN)
        for _ in range(times):
            btn.click()

    def add_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART_BTN)
        self.wait.until(lambda d: d.find_element(*ProductLocators.CART_COUNTER).text.strip().isdigit())

    def view_cart(self):
        self.driver.get(self.base_url + 'shop/cart')

    def decrease_quantity_in_cart(self):
        input_element = self.find(ProductLocators.CART_QTY_INPUT)
        initial_val = input_element.get_attribute("value")
        minus_btn = self.find(ProductLocators.MINUS_BTN)
        self.driver.execute_script("arguments[0].click();", minus_btn)
        self.wait.until(lambda d: d.find_element(*ProductLocators.CART_QTY_INPUT).get_attribute("value") != initial_val)

    def check_quantity_in_cart(self, expected_qty):
        def get_clean_int(locator):
            text = self.get_text(locator).strip()
            return int(re.sub(r'\D', '', text)) if text else 0

        actual_input = int(self.find(ProductLocators.CART_QTY_INPUT).get_attribute("value"))
        self.wait.until(lambda d: get_clean_int(ProductLocators.CART_COUNTER) == expected_qty)

        actual_counter = get_clean_int(ProductLocators.CART_COUNTER)
        assert actual_input == expected_qty
        assert actual_counter == expected_qty

    def go_to_cart_via_header(self):
        icon = self.find(ProductLocators.HEADER_CART_ICON)
        self.driver.execute_script("arguments[0].click();", icon)
        self.wait.until(EC.url_contains("/shop/cart"))

    def remove_item_from_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(ProductLocators.REMOVE_ITEM_BTN))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.invisibility_of_element_located(ProductLocators.CART_PRODUCTS_BLOCK))

    def should_be_empty_cart(self):
        self.wait.until(lambda d: "empty" in d.page_source.lower())
        assert "Your cart is empty!" in self.driver.page_source
