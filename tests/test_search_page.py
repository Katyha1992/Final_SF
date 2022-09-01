from search_page import SearchPage, url_search_page
import pytest
from base_page import BasePage

# Проверка, что в header присутствует строка поиска
def test_45_guest_shold_see_search_input(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.shold_be_search_input()

@pytest.mark.parametrize('input_text', ["кружка",
                                        "КРУЖКА",
                                        "rhe;rf"])
# Проверка, что при вводе товара в поисковую строку на странице выводится найденный товар
# вводим "кружка", "КРУЖКА", "rhe;rf" (test_EXP048_EXP049_EXP050)
def test_46_47_48_search_by_product_name_in_uppercase_and_in_english_layout(browser, input_text):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_product_list(input_text)

# Проверка, что на странице видна информация о количестве найденного товара
def test_49_guest_shold_see_quantity_of_items_found(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_quantity_of_items_found()

# Проверка, количество товара на странице совпадает с количеством в тексте: "Найдено товаров ..."
def test_50_the_number_of_products_on_the_page_is_equal_to_the_number_of_products_found(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.the_number_of_products_on_the_page_is_equal_to_the_number_of_products_found()


@pytest.mark.parametrize('input_text', ["@#₽&+():;!?∆¶×÷π√\}{=°^¢$€£%©®™℅",
                                        "1234567890",
                                        BasePage.symbols_256('self', 's')])
# Негативные сценарии.
# Проверка, что при некорректном вводе на странице появляется сообщение "Ничего не найдено"
def test_51_52_53_with_negative_scenario_should_be_product_not_found(browser, input_text):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_product_not_found(input_text)

# Проверка, что на иконке "Корзина" появляется количество добавленного товара
def test_54_should_be_the_number_of_the_added_product_appears_on_the_Cart_icon(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_the_number_of_the_added_product_appears_on_the_Cart_icon()

# Проверка, что во вкладке корзины присутствует добавленный товар
def test_55_should_be_the_added_product_is_in_the_cart_tab(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_the_added_product_is_in_the_cart_tab()

# python -m pytest -v --tb=line C:/TESTER/final_SF/tests/test_search_page.py