from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_item_name(self,locator):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH,
            f"//div[@data-test='inventory-item-name' and contains(text(),'{locator}')]"))
        )
        return element.text

    def get_item_price(self,locator):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH,
            f"//div[@data-test='inventory-item-price' and contains(.,'{locator}')]"))
        )
        return float(element.text.replace("$","").strip())

    def click_checkout(self):
        self.driver.find_element(By.ID,"checkout").click()

    def has_item(self,item_name):
        for item in self.get_item_names():
            if item == item_name:
                return True
        return False

    def get_item_prices(self):
        elements = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-test='inventory-item-price']"))
        )
        prices = []
        for element in elements:
            prices.append(float(element.text.replace("$","").strip()))
        return prices

    def get_item_names(self):
        elements = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-test='inventory-item-name']"))
        )
        cart = []
        for element in elements:
            cart.append(element.text)
        return cart
