import pytest
from selenium import webdriver

# Фикстура
# После завершения теста, который вызывал фикстуру, выполнение продолжится
# со строки, следующей за строкой со словом yield
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:/TESTER/chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()