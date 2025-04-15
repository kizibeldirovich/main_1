import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_to_cart_redirect(driver):
    driver.get("https://academybugs.com/store/boho-bangle-bracelet/")
    add_to_cart_button = driver.find_element(By.XPATH, "//input[@value='ADD TO CART']")
    add_to_cart_button.click()
    time.sleep(3)
    assert driver.current_url == "https://academybugs.com/my-cart/", f"Перенаправлення не відбулося. Поточна URL: {driver.current_url}"


def test_add_to_cart_and_update_qty(driver):
    driver.get("https://academybugs.com/store/boho-bangle-bracelet/")
    add_to_cart_button = driver.find_element(By.XPATH, "//input[@value='ADD TO CART']")
    add_to_cart_button.click()
    time.sleep(3)

    driver.get("https://academybugs.com/my-cart/")
    time.sleep(3)

    base_price_element = driver.find_element(By.XPATH, "//td[@class='ec_cartitem_price']")
    base_price = float(base_price_element.text.replace('$', '').replace(',', ''))

    # Перевірка кількості від 1 до 2
    for quantity in range(1, 4):
        # Оновлення кількості товару
        for _ in range(quantity - 1):
            plus_button = driver.find_element(By.XPATH, "//input[@value='+']")
            plus_button.click()

        # Оновлення кошика
        update_button = driver.find_element(By.XPATH, "//div[contains(@id, 'ec_cartitem_update')]")
        update_button.click()
        time.sleep(2)

        # Перевірка правильності ціни
        cart_subtotal_element = driver.find_element(By.XPATH, "//div[@id='ec_cart_subtotal']")
        cart_subtotal = float(cart_subtotal_element.text.replace('$', '').replace(',', ''))
        expected_price = base_price * quantity
        assert cart_subtotal == expected_price, f"Ціна в Cart Subtotal для кількості {quantity} не правильна. Очікувана: ${expected_price}, Поточна: ${cart_subtotal}"

        # Виведення інформації
        print(f"Для кількості {quantity}, Cart Subtotal: ${cart_subtotal} - правильна ціна.")

        # Скидання кількості товару
        for _ in range(quantity - 1):
            minus_button = driver.find_element(By.XPATH, "//input[@value='-']")
            minus_button.click()

        time.sleep(1)



def test_search_by_product_title(driver):
    driver.get("https://academybugs.com/store/all-items/#")
    search_input = driver.find_element(By.XPATH, "//input[@class='ec_search_input']")
    search_input.send_keys("Flamingo Tshirt")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)

    # Отримати всі посилання на товари
    results = driver.find_elements(By.XPATH, "//a[contains(text(), 'Flamingo Tshirt')]")

    # Перевірити, що хоча б один результат містить шуканий текст
    assert any("Flamingo Tshirt".lower() in result.text.lower() for result in results), "Product not found!"

    time.sleep(1)

def test_sing_up_button(driver):
    driver.get("https://academybugs.com/store/all-items/#")
    time.sleep(3)
    Sign_up_button = driver.find_element(By.XPATH, '//a[text()="Sign Up"]')
    Sign_up_button.click()
    time.sleep(3)
    Sing_in_button = driver.find_element(By.XPATH, '//div[@class="ec_cart_button_row"]/input[@class="ec_account_button" and @value="SIGN IN"]')
    time.sleep(3)
    Sing_in_button.click()
    time.sleep(3)
    text_1 = driver.find_element(By.ID, 'ec_account_login_email_error').text
    assert text_1 == "Please enter your Email Address"
    # text_2 = driver.find_element(By.ID, 'ec_account_login_password_error').text
    # assert text_2 == "Please enter your Password"

