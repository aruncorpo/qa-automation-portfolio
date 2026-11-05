from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_item(self,add_to_cart_id):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(add_to_cart_id)
        ).click()

    def get_cart_count(self):
        badge = WebDriverWait(self.driver,1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
        )
        return int(badge.text)

    def open_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
