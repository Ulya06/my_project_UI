from pages.base_page import BasePage
from pages.locators.product_locators import ProductLocators


class ProductPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/furn-9999-office-design-software-7?category=9')

    def increase_quantity(self):
        qty_before = int(self.get_attribute(ProductLocators.QTY_INPUT, 'value'))
        self.click(ProductLocators.PLUS_BUTTON)
        return qty_before

    def get_quantity(self):
        return int(self.get_attribute(ProductLocators.QTY_INPUT, 'value'))

    def get_add_button_text(self):
        return self.get_text(ProductLocators.ADD_BUTTON)

    def get_breadcrumb(self):
        return self.get_text(ProductLocators.BREADCRUMB)

    def is_image_visible(self):
        return self.find(ProductLocators.PRODUCT_IMAGE).is_displayed()

    def get_share_links_count(self):
        return len(self.find_all(ProductLocators.SHARE_LINKS))
