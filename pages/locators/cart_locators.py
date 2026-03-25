from selenium.webdriver.common.by import By


class CartLocators:
    EMPTY_CART = (By.CLASS_NAME, 'js_cart_lines')
    HEADER = (By.TAG_NAME, 'h3')
    CONTACT_BTN = (By.CLASS_NAME, 'oe_unremovable')
    SEARCH_BTN = (By.CSS_SELECTOR, 'a[data-bs-toggle="modal"]')
    SEARCH_MODAL = (By.ID, 'o_search_modal')
    WARNING = (By.CSS_SELECTOR, 'div.alert.alert-warning')
