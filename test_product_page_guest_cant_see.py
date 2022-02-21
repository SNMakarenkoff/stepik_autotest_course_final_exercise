from .pages.product_page import ProductPage
import pytest

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
    page = ProductPage(browser, link)
    page.open()
    page.open_product_page()
    page.added_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
    page = ProductPage(browser, link)
    page.open()
    page.open_product_page()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
    page = ProductPage(browser, link)
    page.open()
    page.open_product_page()
    page.added_to_basket()
    page.should_be_disappeared_message()