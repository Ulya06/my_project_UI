from selenium.webdriver.common.by import By


class CartLocators:
    EMPTY_CART = (By.CLASS_NAME, 'js_cart_lines')
    HEADER = (By.TAG_NAME, 'h3')
    CONTACT_BTN = (By.CLASS_NAME, 'oe_unremovable')
    SEARCH_BTN = (By.CSS_SELECTOR, 'a[data-bs-toggle="modal"]')
    SEARCH_MODAL = (By.ID, 'o_search_modal')
    WARNING = (By.CSS_SELECTOR, 'div.alert.alert-warning')
    CATEGORIES_MENU = (By.XPATH, "//a[span[text()='Categories']]")
    DESKS_LINK = (By.CSS_SELECTOR, "ul.dropdown-menu a[href*='desks-1']")
    FURN_LINK = (By.CSS_SELECTOR, "ul.dropdown-menu a[href*='furnitures-2']")
    SUBMIT_BTN = (By.CLASS_NAME, 's_website_form_send')
    FORM_RESULT = (By.CSS_SELECTOR, '#s_website_form_result')
