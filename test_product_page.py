from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_chart()
    page.solve_quiz_and_get_code()
    basket_price = page.get_basket_price()
    book_price = page.get_book_price()
    book_title = page.get_book_title()
    message_book_title = page.get_book_message_title()
    assert book_price == basket_price, "Book price and basket price are different"
    assert book_title == message_book_title, "Book title and message book title are different"
