from selenium.webdriver.common.by import By


class ProductLocators:
    BREADCRUMB = (By.CLASS_NAME, 'breadcrumb')
    PLUS_BTN = (By.CSS_SELECTOR, "a.js_add_cart_json i.fa-plus")
    MINUS_BTN = (By.CSS_SELECTOR, "a.js_add_cart_json i.fa-minus")
    ADD_TO_CART_BTN = (By.ID, "add_to_cart")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/shop/cart']")
    CART_COUNTER = (By.CLASS_NAME, 'my_cart_quantity')
    CART_QTY_INPUT = (By.CSS_SELECTOR, "input.js_quantity")
    PRICELIST_BTN = (By.CSS_SELECTOR, ".o_pricelist_dropdown .dropdown-toggle")
    EUR_PRICELIST = (By.XPATH, "//a[.//span[contains(text(), 'EUR')]]")
    HEADER_CART_ICON = (By.CSS_SELECTOR, "header .fa-shopping-cart")
    REMOVE_ITEM_BTN = (By.CSS_SELECTOR, ".js_delete_product, a[href*='/shop/cart/update_json']")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".js_cart_lines.alert-info, #cart_products + .alert-info")
    CART_PRODUCTS_BLOCK = (By.ID, "cart_products")
