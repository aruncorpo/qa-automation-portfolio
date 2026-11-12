from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_visible_text(self, locator):
        return WebDriverWait(self.driver,4).until(EC.visibility_of_element_located(locator))

    def get_visible_time(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def get_visible_texts(self, locator):
        elements = WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(locator))
        elements_found = []
        for element in elements:
            elements_found.append(element.text)
        return elements_found

    def get_visibility(self, locator):
        try:
            return WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False



