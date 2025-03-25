from selenium.webdriver.common.by import By
from Pages.base_page import BasePage  # Правильный импорт

class HomePage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-form__input.ng-pristine.ng-valid.ng-touched")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".button.button_color_green.button_size_medium.search-form__submit")

    def search(self, query):
        self.enter_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)