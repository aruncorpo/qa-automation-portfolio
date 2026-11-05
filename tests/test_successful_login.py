import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
import data_prep

@pytest.mark.parametrize(
    "logged_in_driver",
        data_prep.get_successful_users()
    ,
    indirect=["logged_in_driver"]
)

def test_initialization(logged_in_driver):

    basepage = BasePage(logged_in_driver)
    inventorypage = InventoryPage(logged_in_driver)
    cartpage = CartPage(logged_in_driver)
    checkoutpage = CheckoutPage(logged_in_driver)
    overviewpage = OverviewPage(logged_in_driver)

    inventorypage.add_item((By.ID, "add-to-cart-sauce-labs-backpack"))
    assert inventorypage.get_cart_count() == 1, "Cart badge no changes"
    inventorypage.open_cart()

    assert cartpage.get_item_name("Sauce Labs Backpack") == "Sauce Labs Backpack", "Item missing"
    assert cartpage.get_item_price("29.99") == 29.99, "Item missing"
    cartpage.click_checkout()

    assert basepage.get_visible_text(
        (By.CSS_SELECTOR, "[data-test='title']")).text == "Checkout: Your Information", "Checkout page not found"
    checkoutpage.enter_customer_information("standard", "user", "123")

    assert basepage.get_visible_text(
        (By.CSS_SELECTOR, "[data-test='title']")).text == "Checkout: Overview", "Checkout: Overview page not found"

    assert overviewpage.get_item_name("Sauce Labs Backpack") == "Sauce Labs Backpack", "Item missing"
    assert overviewpage.get_item_price("29.99") == 29.99, "Item missing"
    assert overviewpage.get_tax() == 2.40, "Value incorrect"
    assert overviewpage.get_total() == pytest.approx(29.99 + 2.40, abs=0.001), "Value incorrect"
    assert overviewpage.get_subtotal() == 29.99, "Value incorrect"
    assert overviewpage.get_payment_info() == "SauceCard #31337", "Value incorrect"
    assert overviewpage.get_shipping_info() == "Free Pony Express Delivery!", "Value incorrect"
    overviewpage.finish()
    assert basepage.get_visible_text((By.CSS_SELECTOR, "[data-test='title']")).text == "Checkout: Complete!"

@pytest.mark.parametrize(
    ("username","password","expected"),
    data_prep.get_test_data()
)
def test_login(driver, username, password, expected):

    loginpage = LoginPage(driver)
    driver.get('https://www.saucedemo.com/')
    loginpage.login(username, password)

    if expected == "success":
        assert loginpage.is_logged_in() == True, "Test Passed"
    elif expected == "locked":
        assert loginpage.get_login_error() == "Epic sadface: Sorry, this user has been locked out."