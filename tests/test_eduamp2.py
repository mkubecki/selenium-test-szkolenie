from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture
def browser():
    driverPath = "/Users/mkubecki/Desktop/Selenium/lib/chromedriver"
    #sciezke do naszego webriver i jego zainicjowanie
    service = Service(executable_path=driverPath)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.maximize_window()
    

def test_method_1(browser):
    browser.get("http://www.eduamp.pl")
    assert browser.title == "eduamp.pl — Szkolenia IT i doradztwo w zakresie IT"



def test_method_2(browser):
    browser.get("http://www.eduamp.pl")
    assert browser.title == "eduamp.pl — Szkolenia IT i doradztwo w zakresie IT"


