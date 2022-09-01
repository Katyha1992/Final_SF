from cart_page import CartPage, url_cart_page

## Проверка корзины ##

# Проверка, что на странице корзины содержится добавленный товар
def test_56_should_see_added_item_in_cart_page(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.should_be_added_item_in_cart()

# Проверка, что кнопка "очистить корзину" удаляет содержимое корзины
def test_57_the_empty_cart_button_deletes_the_contents_of_the_cart(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.should_be_empty_shopping_cart()

# Проверка, что кнопка "оформить заказ" ведет на страницу оформления заказа
def test_58_the_checkout_button_opens_checkout_page(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.the_checkout_button_opens_the_corresponding_page()


    # python -m pytest -v --tb=line  C:/TESTER/final_SF/tests/test_cart_page.py