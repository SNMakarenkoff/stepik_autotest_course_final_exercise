from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Basket is not empty'

    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_BASKET_ITEMS), 'It\s items in basket'