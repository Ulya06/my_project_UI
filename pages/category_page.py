from pages.base_page import BasePage
from pages.locators.category_locators import CategoryLocators


class CategoryPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/category/desks-1')

    def get_products_count(self):
        return len(self.find_all(CategoryLocators.PRODUCTS))

    def get_first_product_name(self):
        return self.get_text(CategoryLocators.FIRST_PRODUCT)

    def open_first_product(self):
        self.click(CategoryLocators.FIRST_PRODUCT)

    def get_breadcrumb(self):
        return self.get_text(CategoryLocators.BREADCRUMB)

    def change_currency_to_eur(self):
        self.click(CategoryLocators.DROPDOWN)
        self.click(CategoryLocators.EUR_OPTION)

    def get_price_text(self):
        return self.get_text(CategoryLocators.PRICE)
