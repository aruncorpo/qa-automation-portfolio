from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        userid = "user-name"
        passwordid = "password"
        loginid = "login-button"

        self.driver.find_element(By.ID, userid).send_keys(username)
        self.driver.find_element(By.ID, passwordid).send_keys(password)
        self.driver.find_element(By.ID, loginid).click()

    def is_logged_in(self):
        inventory_title = WebDriverWait(self.driver,3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']"))
        )
        return inventory_title.text == "Products"

    def get_login_error(self):
        error = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test = 'error']")
        return error.text

    def logout(self,):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        located = WebDriverWait(self.driver,3).until(
                EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
            )
        located.click()