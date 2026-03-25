from selenium.webdriver.common.by import By


class ProductLocators:
    ADD_BUTTON = (By.ID, 'add_to_cart')
    PLUS_BUTTON = (By.CSS_SELECTOR, 'a.js_add_cart_json[aria-label="Add one"]')
    QTY_INPUT = (By.CSS_SELECTOR, 'input[name="add_qty"]')
    BREADCRUMB = (By.CSS_SELECTOR, 'ol.breadcrumb')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.product_detail_img')
    SHARE_LINKS = (By.CSS_SELECTOR, '.s_share a')
