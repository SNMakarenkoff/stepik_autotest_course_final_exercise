from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def added_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()

    def should_be_same_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_check = self.browser.find_element(*ProductPageLocators.BOOK_NAME_CHECK)
        assert book_name.text == book_name_check.text, 'Название книги в корзине не совпадает с выбранной'

    def should_be_same_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_check = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_CHECK)
        assert book_price.text == book_price_check.text, 'Цена книги в корзине не совпадает с выбранной'

    def open_product_page(self):
        open_product = self.browser.find_element(*ProductPageLocators.OPEN_PRODUCT_PAGE)
        open_product.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"