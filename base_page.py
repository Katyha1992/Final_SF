from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators import BasePageLocators, SearchPageLocators, LoginDialogBoxPageLocators
from selenium.webdriver.common.by import By

# создаем конструктор, который принимает browser — экземпляр webdriver.
# Указываем url, который будет использоваться для открытия страницы.
class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 5c:
        self.browser.implicitly_wait(timeout)

    # создаем метод find_element (ищет один элемент и возвращает его)
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # создаем метод find_elements (ищет множество элементов и возвращает в виде списка)
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # метод open должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # метод is_element_present перехватывает исключение.
    # будет использоваться для проверки присутствия элемента на странице
    # В него будем передавать два аргумента: как искать и собственно что искать.
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # метод is_not_element_present будет использоваться для проверки отсутствия элемента на странице
    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return True
        return False

    # метод для получения 256 символов
    def symbols_256(self, symbol):
        symbols = symbol * 256
        return symbols

######## ДАЛЕЕ ИДУТ ОБЩИЕ ДЛЯ ВСЕХ СТРАНИЦ МЕТОДЫ ПРОВЕРОК ###########

    # Метод проверки, что в header присутствует кнопка "прайс-лист"
    def should_be_button_price_list(self):
        button = self.find_element(BasePageLocators.BUTTON_PRISE_LIST)
        result = button.text
        assert "ПРАЙС-ЛИСТ" == result

    # Метод проверки, что при нажатии на кнопку "прайс-лист" открывается форма для заполнения
    def the_price_list_button_opens_the_form_for_receiving_price_list(self):
        button = self.find_element(BasePageLocators.BUTTON_PRISE_LIST)
        button.click()
        assert self.is_element_present(*BasePageLocators.FORM_PRISE_LIST), "Form prise_list is not presented"

    # Метод проверки, что в header присутствует кнопка выпадающего списка "ИНФОРМАЦИЯ"
    def should_be_information_list(self):
        button = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        button.click()
        result = button.text
        assert "ИНФОРМАЦИЯ" == result

    # Метод проверки, что в выпадающем списке "ИНФОРМАЦИЯ" есть 3 элемента
    def should_be_information_list_has_three_elements(self):
        button = self.find_elements(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        result = len(button) - 1
        assert result == 3

    # Метод проверки, что кнопка "Доставка" в выпадающем списке "ИНФОРМАЦИЯ" ведет на соотв.страницу
    def the_link_dostavka_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/dostavka/"
        link = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        link.click()
        dostavka_link = self.find_element(BasePageLocators.InformationListLocators.DOSTAVKA_LINK)
        dostavka_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что кнопка "Оплата" в выпадающем списке "ИНФОРМАЦИЯ" ведет на соотв.страницу
    def the_link_oplata_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/oplata/"
        link = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        link.click()
        oplata_link =self.find_element(BasePageLocators.InformationListLocators.OPLATA_LINK)
        oplata_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что кнопка "Обмен и возврат" в выпадающем списке "ИНФОРМАЦИЯ" ведет на соотв.страницу
    def the_link_obmen_vozvrat_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/usloviya-vozvrata/"
        link = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        link.click()
        obmen_vozvrat_link = self.find_element(BasePageLocators.InformationListLocators.OBMEN_VOZVRAT_LINK)
        obmen_vozvrat_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что в header присутствует геолокация
    def should_be_geolocation_map(self):
        map = self.find_element(BasePageLocators.GEOLOCATION_MAP)
        result = map.text
        assert result != ''

    # Метод проверки, что ссылка на геолокацию открывает окно геолокации
    def the_link_geolocation_map_opens_window_with_geolocation_map(self):
        link = self.find_element(BasePageLocators.GEOLOCATION_MAP)
        link.click()
        assert self.is_element_present(By.CSS_SELECTOR, "#ui-id-1"), "Window with geolocation map is not presented"

    # Метод проверки, что в header присутствует кнопка "новинки"
    def should_be_novinki_link(self):
        link = self.find_element(BasePageLocators.NOVINKI_LINK)
        result = link.text
        assert "Новинки" == result

    # Метод проверки, что ссылка "новинки" открывает страницу с новыми поступлениями
    def the_novinki_link_open_page_noviepostupleniya(self):
        url = "https://besttea.ru/noviepostupleniya/"
        link = self.find_element(BasePageLocators.NOVINKI_LINK)
        link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что в header присутствует кнопка "Скидки"
    def should_by_sale_link(self):
        link = self.find_element(BasePageLocators.SALE_LINK)
        result = link.text
        assert "Скидки" == result

    # Метод проверки, что ссылка "Скидки" открывает нужную страницу
    def the_sale_link_opens_the_corresponding_page(self):
        url = "https://besttea.ru/sale/"
        link = self.find_element(BasePageLocators.SALE_LINK)
        link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что в header присутствует кнопка выпадающего списка "Оптовикам"
    def should_by_optovikam_list(self):
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        result = optovikam_list.text
        assert "Оптовикам" == result

    # Метод проверки, что в выпадающем списке "Оптовикам" есть пять элементов
    def should_be_optovikam_list_has_five_elements(self):
        button = self.find_elements(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        result = len(button) - 1
        assert result == 5

    # Метод проверки, что ссылка "Чай оптом" в выпадающем списке "Оптовикам" ведет на соотв.страницу
    def the_link_chai_optom_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/opt/"
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        chai_optom_link = self.find_element(BasePageLocators.OptovikamListLocators.CHAI_OPTOM_LINK)
        chai_optom_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Кофе оптом" в выпадающем списке "Оптовикам" ведет на соотв.страницу
    def the_link_kofe_optom_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/opt/kupit-kofe-optom/"
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        kofe_optom_link = self.find_element(BasePageLocators.OptovikamListLocators.KOFE_OPTOM_LONK)
        kofe_optom_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Посуда оптом" в выпадающем списке "Оптовикам" ведет на соотв. страницу
    def the_link_posuda_optom_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/opt/posuda-is-stekla-optom/"
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        posuda_optom_link = self.find_element(BasePageLocators.OptovikamListLocators.POSUDA_OPTOM_LINK)
        posuda_optom_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Производство чая BestTea" в выпадающем списке "Оптовикам" ведет на соотв. страницу
    def the_link_proizvodstvo_opens_the_corresponding_page(self):
        url = "https://besttea.ru/proizvodstvo-chaya/"
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        proizvodstvo_link = self.find_element(BasePageLocators.OptovikamListLocators.PROIZVODSTVO_LINK)
        proizvodstvo_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Сертификаты и Декларации" в выпадающем списке "Оптовикам" ведет на соотве. страницу
    def the_link_sertifikaty_i_deklaracii_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/sertifikatyi/"
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        sertifikaty_link = self.find_element(BasePageLocators.OptovikamListLocators.SERTIFIKATY_LINK)
        sertifikaty_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что в header присутствует кнопка "Контакты"
    def should_by_Kontakty_link(self):
        kontakty_link = self.find_element(BasePageLocators.KONTAKTY_LINK)
        result = kontakty_link.text
        assert result == "Контакты"

    # Метод проверки, что ссылка "Контакты" ведет на соотв.страницу
    def the_link_kontakty_opens_the_corresponding_page(self):
        url = "https://besttea.ru/contact/"
        kontakty_link = self.find_element(BasePageLocators.KONTAKTY_LINK)
        kontakty_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что в header присутствует ссылка "Посмотреть список отложенных товаров"
    def should_by_wish_list_link(self):
        assert self.is_element_present(*BasePageLocators.WishList.WISH_LIST_LINK), "Wish list link is not presented"

    # Метод проверки, что ссылка "Посмотреть список отложенных товаров" ведет на соотв. страницу
    def the_link_wish_list_opens_the_corresponding_page(self):
        url = "https://besttea.ru/wishlist/"
        wish_list_link = self.find_element(BasePageLocators.WishList.WISH_LIST_LINK)
        wish_list_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что на иконке "список отложенных товаров" не присутсвует цифра
     # обозначающая количество отложенных товаров
    def not_should_by_number_in_wish_list_if_not_adding_product(self):
        assert self.is_not_element_present(*BasePageLocators.WishList.WISH_LIST_LINK_COUNT), \
            "there is a value with the amount of added product"

    # Метод проверки, что в header присутствует кнопка выпадающего списка "Каталог товаров"
    def should_by_katalog_tovarov_list(self):
        katalog_link = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        result = katalog_link.text
        assert "Каталог товаров" == result

    # Метод проверки, что в выпадающем списке "Каталог товаров" есть шесть элементов
    def should_be_in_katalog_tovarov_list_six_elements(self):
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        katalog_list = self.find_elements(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST)
        result = len(katalog_list)
        assert result == 6

    # Метод проверки, что ссылка "Чай" ведет на соотв. страницу
    def the_link_chai_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/elitniy-chay/'
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        chai_link = self.find_element(BasePageLocators.KatalogTovarovListLocators.CHAI_LINK)
        chai_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Кофе" ведет на соотв. страницу
    def the_link_kofe_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/zernovoi-kofe/'
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        kofe_link = self.find_element(BasePageLocators.KatalogTovarovListLocators.KOFE_LINK)
        kofe_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Мате" ведет на соотв. страницу
    def the_link_mate_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/mate-i-prinadlejnosti/'
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        mate_link = self.find_element(BasePageLocators.KatalogTovarovListLocators.MATE_LINK)
        mate_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Сладости" ведет на соотв. страницу
    def the_link_sladosti_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/sladosti/'
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        sladosti_link = self.find_element(BasePageLocators.KatalogTovarovListLocators.SLADOSTI_LINK)
        sladosti_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Посуда и аксессуары" ведет на соотв. страницу
    def the_link_posuda_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/posuda-i-prinadlezhnosti/'
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        posuda_link = self.find_element(BasePageLocators.KatalogTovarovListLocators.POSUDA_LINK)
        posuda_link.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что ссылка "Хранение и упаковка" ведет на соотв.страницу
    def the_link_upakovka_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/torgovoe-oborudovanie/'
        katalog_list_button = self.find_element(BasePageLocators.KatalogTovarovListLocators.KATALOG_TOVAROV_LIST_BUTTON)
        katalog_list_button.click()
        upakovka_list = self.find_element(BasePageLocators.KatalogTovarovListLocators.UPAKOVKA_LINK)
        upakovka_list.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что присутствует строка поиска
    def should_be_search_input(self):
        assert self.is_element_present(*BasePageLocators.SearchLokators.SERCH_INPUT), "Wish serch input is not presented"

    # Метод проверки, что при нажатии на иконку поиск происходит переход на страницу поиска
    def the_search_icon_opens_the_serch_page(self):
        url = 'https://besttea.ru/search/?match=all&subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q=&security_hash=e88f11571835a13bf19ece501d130d66'
        search_button = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        search_button.click()
        search_text = self.find_element(SearchPageLocators.SEARCH_PAGE_TEXT)
        result = search_text.text
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert "Результаты поиска" == result

    # Метод проверки, что присутствует выпадающий список "Аккаунт"
    def should_be_account_list(self):
        account_button = self.find_element(BasePageLocators.AccountLokators.ACCOUNT_BUTTON)
        result = account_button.text
        assert 'Аккаунт' == result

    # Метод проверки, что в выпадающем списке "Аккаунт" присутствует 3 ссылки
    def should_be_in_account_list_three_links(self):
        account_button = self.find_element(BasePageLocators.AccountLokators.ACCOUNT_BUTTON)
        account_button.click()
        account_list = self.find_elements(BasePageLocators.AccountLokators.ACCOUN_LIST)
        result = len(account_list)
        assert result == 3

    # Метод проверки, что в выпадающем списке "Аккаунт" присутствует кнопка "Войти"
    def should_be_in_account_list_login_button(self):
        account_button = self.find_element(BasePageLocators.AccountLokators.ACCOUNT_BUTTON)
        account_button.click()
        login_button = self.find_element(BasePageLocators.AccountLokators.LOGIN_BUTTON)
        result = login_button.text
        assert 'Войти' == result

    # Метод проверки, что в выпадающем списке "Аккаунт" присутствует кнопка "Регистрация"
    def should_be_in_account_list_registration_button(self):
        account_button = self.find_element(BasePageLocators.AccountLokators.ACCOUNT_BUTTON)
        account_button.click()
        registration_button = self.find_element(BasePageLocators.AccountLokators.REGISTRATION_BUTTON)
        result = registration_button.text
        assert 'Регистрация' == result

    # Метод проверки, что кнопка "Войти" открывает форму авторизации
    def button_login_in_account_list_opens_login_dialog_box(self):
        account_button = self.find_element(BasePageLocators.AccountLokators.ACCOUNT_BUTTON)
        account_button.click()
        login_button = self.find_element(BasePageLocators.AccountLokators.LOGIN_BUTTON)
        login_button.click()
        login_dialog_box = self.find_element(LoginDialogBoxPageLocators.LOGIN_DIALOG_BOX)
        result = login_dialog_box.text
        assert 'Войти' == result

    # Метод проверки, что кнопка "Регистрация" открывает страницу регистрации
    def button_registration_in_account_list_opens_registration_page(self):
        url = 'https://besttea.ru/profiles-add/'
        account_button = self.find_element(BasePageLocators.AccountLokators.ACCOUNT_BUTTON)
        account_button.click()
        registration_button = self.find_element(BasePageLocators.AccountLokators.REGISTRATION_BUTTON)
        registration_button.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

    # Метод проверки, что присутствует выпадающий список "Корзина"
    def should_be_korzina_list(self):
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_text = korzina_button.text
        result = korzina_text.split()
        assert result[1] == 'Корзина'

    # Метод проверки, что в выпадающем списке "Корзина" присутствует текст "Корзина пуста"
    def should_be_in_korzina_list_text_korzina_pusta(self):
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_button.click()
        korzina_list = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_LIST)
        result = korzina_list.text
        assert  result == 'Корзина пуста'