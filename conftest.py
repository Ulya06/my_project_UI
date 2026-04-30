import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
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
