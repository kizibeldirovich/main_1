import pytest
from Pages.home_page import HomePage  # Импорт из каталога Pages

def test_search_product(driver):
    home_page = HomePage(driver)
    home_page.open("https://rozetka.com.ua/ua/promo/sunnydiscounts/")
    home_page.search("куртка")
    assert "куртка" in driver.title.lower(), "Пошук не працює!"