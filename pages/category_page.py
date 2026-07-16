from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.category_locators import CategoryLocators


class CategoryPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/category/desks-1')

    def verify_product_name_in_source(self, name):
        self.wait.until(
            EC.visibility_of_element_located(
                CategoryLocators.PRODUCT_NAME
            )
        )
        assert name in self.driver.page_source

    def open_first_product(self):
        self.click(CategoryLocators.PRODUCT_NAME)

    def change_currency_to_eur(self):
        self.click(CategoryLocators.PRICELIST_BTN)

        element = self.wait.until(
            EC.element_to_be_clickable(
                CategoryLocators.EUR_PRICELIST
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def should_all_prices_be_in_eur(self):
        self.wait.until(
            lambda driver: "€" in driver.page_source
        )

        assert "€" in self.driver.page_source
