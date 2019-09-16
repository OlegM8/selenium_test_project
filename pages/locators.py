from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")
    ADDED_BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color:nth-child(2)")
    BASKET = (By.XPATH, "//*[@class='basket-mini pull-right hidden-xs']")