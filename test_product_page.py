from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    basket_price = page.get_basket_price()
    book_price = page.get_book_price()
    book_title = page.get_book_title()
    message_book_title = page.get_book_message_title()
    assert book_price == basket_price, "Book price and basket price are different"
    assert book_title == message_book_title, "Book title and message book title are different"
