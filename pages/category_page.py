from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.category_locators import CategoryLocators


class CategoryPage(BasePage):
    def open_page(self):
        self.open(self.base_url + 'shop/category/desks-1')

    def verify_product_name_in_source(self, name):
        self.wait.until(
            EC.visibility_of_element_located(CategoryLocators.PRODUCT_NAME)
        )
        assert name in self.driver.page_source

    def open_first_product(self):
        self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.PRODUCT_NAME)
        ).click()

    def switch_to_list_view(self):
        self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.LIST_VIEW_BTN)
        ).click()

        self.wait.until(
            EC.presence_of_element_located(
                CategoryLocators.LIST_VIEW_CONTAINER
            )
        )

    def select_steel_filter(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.STEEL_CHECKBOX)
        )

        self.driver.execute_script("arguments[0].click();",checkbox)

        self.wait.until(EC.url_contains("attrib=1-1"))

    def click_cart_icon(self):
        icon = self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.ADD_TO_CART_ICON)
        )

        self.driver.execute_script("arguments[0].click();",icon)

    def proceed_to_checkout(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.PROCEED_CHECKOUT_BTN)
        )
        btn.click()

    def should_be_on_cart_page(self):
        self.wait.until(EC.url_contains("/shop/cart"))

    def verify_product_in_cart(self, full_name, description):
        title = self.get_text(CategoryLocators.CART_PRODUCT_TITLE)
        desc = self.get_text(CategoryLocators.CART_PRODUCT_DESCRIPTION)

        assert full_name in title
        assert description in desc

    def change_currency_to_eur(self):
        self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.PRICELIST_BTN)
        ).click()

        eur = self.wait.until(
            EC.element_to_be_clickable(CategoryLocators.EUR_PRICELIST)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            eur
        )

    def should_all_prices_be_in_eur(self):
        self.wait.until(
            lambda driver: "€" in driver.page_source
        )

        assert "€" in self.driver.page_source
