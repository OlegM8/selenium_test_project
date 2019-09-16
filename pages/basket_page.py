from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        basket_status = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        assert 'Your basket is empty.' in basket_status, "Basket is not empty!"
