from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_book_to_basket(self):
        add_book_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_book_button.click()

    def success_message_is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def book_and_basket_price_should_be_equal(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket = self.browser.find_element(*ProductPageLocators.BASKET).text
        basket_price = basket.split()
        assert book_price == basket_price[2],  "Book price and basket price are different"

    def book_title_must_be_same_as_in_message(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_message_title = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_MESSAGE).text
        assert book_title == book_message_title, "Book title and message book title are different"
