from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.category_locators import CategoryLocators


class CategoryPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/category/desks-1')

    def change_currency_to_eur(self):
        self.click(CategoryLocators.PRICELIST_BTN)
        element = self.wait.until(EC.element_to_be_clickable(CategoryLocators.EUR_PRICELIST))
        self.driver.execute_script("arguments[0].click();", element)

    def should_all_prices_be_in_eur(self):
        self.wait.until(EC.presence_of_all_elements_located(CategoryLocators.PRICE))
        assert '€' in self.driver.page_source

    def get_first_product_name(self):
        return self.get_text(CategoryLocators.PRODUCT_NAME)

    def open_first_product(self):
        self.click(CategoryLocators.PRODUCT_NAME)

    def switch_to_list_view(self):
        btn = self.wait.until(EC.element_to_be_clickable(CategoryLocators.LIST_VIEW_BTN))
        btn.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".o_wsale_layout_list")))

    def select_steel_filter(self):
        checkbox = self.wait.until(EC.presence_of_element_located(CategoryLocators.STEEL_CHECKBOX))
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait.until(EC.url_contains("attrib=1-1"))

    def click_cart_icon(self):
        icon = self.wait.until(EC.element_to_be_clickable(CategoryLocators.ADD_TO_CART_ICON))
        self.driver.execute_script("arguments[0].click();", icon)

    def proceed_to_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable(CategoryLocators.PROCEED_CHECKOUT_BTN))
        btn.click()

    def should_be_on_cart_page(self):
        self.wait.until(EC.url_contains("/shop/cart"))
        assert "/shop/cart" in self.driver.current_url

    def verify_product_in_cart(self, full_name, description):
        title = self.wait.until(EC.visibility_of_element_located(CategoryLocators.CART_PRODUCT_TITLE)).text
        desc = self.driver.find_element(*CategoryLocators.CART_PRODUCT_DESCRIPTION).text
        assert full_name in title
        assert description in desc

    def get_price_text(self):
        return self.get_text(CategoryLocators.PRICE)
