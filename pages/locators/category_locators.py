from selenium.webdriver.common.by import By


class CategoryLocators:
    PRICE = (By.CLASS_NAME, 'oe_currency_value')
    PRODUCT_NAME = (By.CLASS_NAME, 'o_wsale_products_item_title')
    PRICELIST_BTN = (By.CSS_SELECTOR, '.o_pricelist_dropdown .dropdown-toggle')
    EUR_PRICELIST = (By.XPATH, "//a[.//span[contains(text(), 'EUR')]]")
    STEEL_CHECKBOX = (By.CSS_SELECTOR, "input[value='1-1']")
    ADD_TO_CART_ICON = (By.CSS_SELECTOR, ".o_wsale_product_btn .a-submit")
    PROCEED_CHECKOUT_BTN = (By.CSS_SELECTOR, ".o_sale_product_configurator_edit")
    CART_PRODUCT_TITLE = (By.CSS_SELECTOR, ".o_cart_product h6")
    CART_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".o_cart_product .text-muted")
    LIST_VIEW_BTN = (By.CSS_SELECTOR, ".o_wsale_view_list")
    LIST_VIEW_CONTAINER = (By.CSS_SELECTOR, ".o_wsale_layout_list")
