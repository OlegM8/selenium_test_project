from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_book_to_basket(self):
        add_book_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_book_button.click()

    def get_basket_price(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET).text
        price = basket.split()
        return price[2]

    def get_book_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return price

    def get_book_message_title(self):
        title = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_MESSAGE).text
        return title

    def get_book_title(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        return title

    def success_message_is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"
