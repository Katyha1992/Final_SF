from main_page import MainPage, url_main_page
import pytest

# Проверка, что в header присутствует кнопка "прайс-лист"
def test_1_guest_should_see_in_header_button_price_list(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_button_price_list()

# Проверка, что при нажатии на кнопку "прайс-лист" открывается форма для заполнения
def test_2_the_price_list_button_opens_the_price_list_form(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_price_list_button_opens_the_form_for_receiving_price_list()

# Проверяем выпадающий список "ИНФОРМАЦИЯ"
@pytest.mark.information_list
class TestInformationListFromMainPage():
    # Проверка, что в header присутствует кнопка "ИНФОРМАЦИЯ"
    def test_3_guest_should_see_in_header_information_list(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_information_list()
    # Проверка, что в выпадающем списке "ИНФОРМАЦИЯ" есть 3 элемента
    def test_4_guest_should_see_in_information_list_three_elements(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_information_list_has_three_elements()
    # Проверка, что кнопка "Доставка" ведет на соотв.страницу
    def test_5_the_link_dostavka_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_dostavka_opens_the_corresponding_page()
    # Проверка, что кнопка "Обмен и возврат" ведет на соотв.страницу
    def test_6_the_link_obmen_vozvrat_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_obmen_vozvrat_opens_the_corresponding_page()

        # python -m pytest -v --tb=line -m information_list C:/TESTER/final_SF/tests/test_main_page.py
    # Проверка, что кнопка "Оплата" ведет на соотв.страницу
    def test_7_the_link_oplata_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_oplata_opens_the_corresponding_page()


# Проверка, что в header присутствует геолокация
def test_8_guest_should_see_geolocation_map_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_geolocation_map()

# Проверка, что ссылка на геолокацию открывает окно геолокации
def test_9_link_geolocation_map_opens_window_with_geolocation_map(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_link_geolocation_map_opens_window_with_geolocation_map()

# Проверка, что в header присутствует кнопка "новинки"
def test_10_guest_should_see_in_header_novinki_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_novinki_link()

# Проверка, что ссылка "новинки" открывает страницу с новыми поступлениями
def test_11_novinki_link_open_page_noviepostupleniya(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_novinki_link_open_page_noviepostupleniya()

# Проверка, что в header присутствует кнопка "Скидки"
def test_12_guest_should_see_in_header_sale_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_by_sale_link()

# Проверка, что ссылка "Скидки" открывает нужную страницу
def test_13_sale_link_open_page_sale(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_sale_link_opens_the_corresponding_page()

# Проверяем выпадающий список "Оптовикам"
@pytest.mark.optovikam_list
class TestOptovikamListFromMainPage():
    # Проверка, что в header присутствует кнопка выпадающего списка "Оптовикам"
    def test_14_guest_should_see_in_header_optovikam_list(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_optovikam_list()
    # Проверка, что в выпадающем списке "Оптовикам" есть пять элементов
    def test_15_guest_should_see_in_optovikam_list_five_elements(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_optovikam_list_has_five_elements()
    # Проверка, что ссылка "Чай оптом" ведет на соотв.страницу
    def test_16_the_link_chai_optom_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_chai_optom_opens_the_corresponding_page()
   # Проверка, что ссылка "Кофе оптом" ведет на соотв.страницу
    def test_17_the_link_kofe_optom_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_kofe_optom_opens_the_corresponding_page()
    # Проверка, что ссылка "Посуда оптом" ведет на соотв. страницу
    def test_18_the_link_posuda_optom_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_posuda_optom_opens_the_corresponding_page()
    # Проверка, что ссылка "Производство чая BestTea" ведет на соотв. стран
    def test_19_the_link_proizvodstvo_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_proizvodstvo_opens_the_corresponding_page()
    # Метод проверки, что ссылка "Сертификаты и Декларации" ведет на соотве. страницу
    def test_20_the_link_sertifikaty_i_deklaracii_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_sertifikaty_i_deklaracii_opens_the_corresponding_page()

        # python -m pytest -v --tb=line -m optovikam_list C:/TESTER/final_SF/tests/test_main_page.py

# Проверка, что в header присутствует ссылка "Контакты"
def test_21_guest_should_see_in_header_kontakty_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_by_Kontakty_link()

# Проверка, что ссылка "Контакты" ведет на соотв.страницу
def test_22_the_link_kontakty_opens_the_corresponding_page(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_link_kontakty_opens_the_corresponding_page()

@pytest.mark.wish_list
class TestWishListMainPage():
    # Проверка, что в header присутствует ссылка "Посмотреть список отложенных товаров"
    def test_23_guest_should_see_wish_list_link(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_wish_list_link()
    # Проверка, что ссылка "Посмотреть список отложенных товаров" ведет на соотв. страницу
    def test_24_the_link_wish_list_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_wish_list_opens_the_corresponding_page()
    # Проверка, что на иконке "список отложенных товаров" не присутсвует цифра
    # обозначающая количество отложенных товаров
    def test_25_guest_not_should_see_in_wish_list_link_number(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.not_should_by_number_in_wish_list_if_not_adding_product()
    # Проверка, что в header на иконке ссылки "Посмотреть список отложенных товаров" появилась цифра 1
    def test_26_guest_should_see_in_wish_list_link_number_one(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_number_one_in_wish_list_when_adding_product()

        # python -m pytest -v --tb=line -m wish_list C:/TESTER/final_SF/tests/test_main_page.py

# Проверяем выпадающий список "Каталог товаров"
@pytest.mark.katalog_tovarov_list
class TestKatalogTovarovListMainPage():
    # Проверка, что в header присутствует кнопка выпадающего списка "Каталог товаров"
    def test_27_guest_should_see_katalog_tovarov_list_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_katalog_tovarov_list()
    # Проверка, что в выпадающем списке "Каталог товаров" есть шесть сылок
    def test_28_guest_should_see_in_katalog_tovarov_list_six_links(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_katalog_tovarov_list_six_elements()
    # Проверка, что ссылка "Чай" ведет на соотв. страницу
    def test_29_the_link_chai_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_chai_opens_the_corresponding_page()
    # Проверка, что ссылка "Кофе" ведет на соотв. страницу
    def test_30_the_link_kofe_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_kofe_opens_the_corresponding_page()
    # Проверка, что ссылка "Мате" ведет на соотв. страницу
    def test_31_the_link_mate_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_mate_opens_the_corresponding_page()
    # Проверка, что ссылка "Сладости" ведет на соотв. страницу
    def test_32_the_link_sladosti_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_sladosti_opens_the_corresponding_page()
    # Проверка, что ссылка "Посуда и аксессуары" ведет на соотв. страницу
    def test_33_the_link_posuda_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_posuda_opens_the_corresponding_page()
    # Проверка, что ссылка "Хранение и упаковка" ведет на соотв.страницу
    def test_34_the_link_upakovka_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_upakovka_opens_the_corresponding_page()

        # python -m pytest -v --tb=line -m katalog_tovarov_list C:/TESTER/final_SF/tests/test_main_page.py

@pytest.mark.search_input
class TestSerchInputMainPage():
    # Проверка, что присутствует строка поиска
    def test_35_guest_should_see_search_input(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_search_input()
    # Проверка, что при нажатии на иконку поиск происходит переход на страницу поиска
    def test_36_the_search_icon_opens_the_search_page_when_you_press(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_search_icon_opens_the_serch_page()

        # python -m pytest -v --tb=line -m search_input C:/TESTER/final_SF/tests/test_main_page.py

@pytest.mark.account_list
class TestAccountList():
    # Проверка, что есть выпадающий список "Аккаунт"
    def test_37_guest_should_see_account_list_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_account_list()
    # Проверка, что в выпадающем списке "Аккаунт" присутствует 3 ссылки
    def test_38_should_be_in_account_list_three_links(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_account_list_three_links()
    # Проверка, что в выпадающем списке "Аккаунт" присутствует кнопка "Войти"
    def test_39_guest_should_see_in_account_list_login_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_account_list_login_button()
    # Проверка, что в выпадающем списке "Аккаунт" присутствует кнопка "Регистрация"
    def test_40_guest_should_see_in_account_list_registration_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_account_list_registration_button()
    # Проверка, что кнопка "Войти" открывает форму авторизации
    def test_41_button_login_in_account_list_opens_login_dialog_box(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.button_login_in_account_list_opens_login_dialog_box()
    # Ппроверка, что кнопка "Регистрация" открывает страницу регистрации
    def test_42_button_registration_in_account_list_opens_registration_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.button_registration_in_account_list_opens_registration_page()

        # python -m pytest -v --tb=line -m account_list C:/TESTER/final_SF/tests/test_main_page.py

@pytest.mark.korzina_list
class TestKorzinaList():
    # Проверка, что присутствует выпадающий список "Корзина"
    def test_43_guest_should_see_korzina_list_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_korzina_list()
    # Проверка, что в выпадающем списке "Корзина" присутствует текст "Корзина пуста"
    def test_44_guest_should_see_in_korzina_list_text_korzina_pusta(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_korzina_list_text_korzina_pusta()

        # python -m pytest -v --tb=line -m korzina_list C:/TESTER/final_SF/tests/test_main_page.py


# python -m pytest -v --tb=line  C:/TESTER/final_SF/tests/test_main_page.py

