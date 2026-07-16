import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("window-size = 1920, 1080")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    allure.attach(chrome_driver.get_screenshot_as_png(), name = "screenshot", attachment_type=AttachmentType.PNG)
    chrome_driver.quit()

@pytest.fixture()
def cart_page(driver):
    page = CartPage(driver)
    page.open_page()
    return page

@pytest.fixture()
def category_page(driver):
    page = CategoryPage(driver)
    page.open_page()
    return page

@pytest.fixture()
def product_page(driver):
    page = ProductPage(driver)
    page.open_page()
    return page
