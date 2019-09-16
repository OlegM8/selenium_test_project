from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") #id_registration-email
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")
    ADDED_BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color:nth-child(2)")
    BASKET = (By.XPATH, "//*[@class='basket-mini pull-right hidden-xs']")


class BasketPageLocators():
    BASKET_STATUS = (By.CSS_SELECTOR, "#content_inner p")