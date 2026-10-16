from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_initialization(driver):
    driver.get('https://the-internet.herokuapp.com/iframe?utm_source=chatgpt.com')
    text = driver.find_element(By.XPATH,"//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']").text
    assert text == "An iFrame containing the TinyMCE WYSIWYG Editor", "Text not found"

    WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']"))).click()

    if WebDriverWait(driver,1).until(
            EC.invisibility_of_element_located((By.XPATH,
            "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']"))):

        new_frame = driver.find_element(By.ID,"mce_0_ifr")
        try:
            driver.switch_to.frame(new_frame)
            switched = True
        except NoSuchElementException:
            switched = False

        assert switched,"switch to iframe failed"
        text2 = driver.find_element(By.XPATH, "//p[text()='Your content goes here.']").text
        assert text2 == "Your content goes here.", "Text not found"

        driver.switch_to.default_content()
        text = driver.find_element(By.XPATH, "//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']").text
        assert text == "An iFrame containing the TinyMCE WYSIWYG Editor", "Text not found"
    else:
        print("Popup close failed")