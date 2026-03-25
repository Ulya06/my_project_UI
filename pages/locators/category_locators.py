from selenium.webdriver.common.by import By


class CategoryLocators:
    PRODUCTS = (By.CSS_SELECTOR, 'td.oe_product')
    FIRST_PRODUCT = (By.CSS_SELECTOR, 'td.oe_product h6 a')
    BREADCRUMB = (By.CSS_SELECTOR, 'ol.breadcrumb')
    PRICE = (By.CSS_SELECTOR, 'span.h6.mb-0')
    DROPDOWN = (By.CSS_SELECTOR, '.o_pricelist_dropdown .dropdown-toggle')
    EUR_OPTION = (By.XPATH, "//span[text()='EUR']/ancestor::a")
