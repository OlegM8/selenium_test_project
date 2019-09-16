from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def get_basket_status(self):
        basket_status = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        return basket_status