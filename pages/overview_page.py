from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver

    def get_item_name(self, locator):
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

    def get_tax(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='tax-label']"))
        )
        return float(element.text.replace("Tax: $","").strip())

    def get_total(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='total-label']"))
        )
        return float(element.text.replace("Total: $","").strip())

    def get_subtotal(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='subtotal-label']"))
        )
        return float(element.text.replace("Item total: $","").strip())

    def get_payment_info(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='payment-info-value']"))
        )
        return element.text

    def get_shipping_info(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='shipping-info-value']"))
        )
        return element.text

    def finish(self):
        self.driver.find_element(By.ID,"finish").click()