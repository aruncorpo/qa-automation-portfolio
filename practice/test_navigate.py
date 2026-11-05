from selenium.webdriver.common.by import By

def test_initialization(driver):
    driver.get('https://the-internet.herokuapp.com/')
    driver.find_element(By.LINK_TEXT,"A/B Testing").click()
    driver.back()
    title = driver.find_element(By.XPATH, "//h1[text()='Welcome to the-internet']")
    assert title.text == 'Welcome to the-internet', "Failed to go back"
    driver.forward()
    title1 = driver.find_element(By.XPATH, "//p[contains(text(), 'split testing')]")
    assert "split testing" in title1.text, "Forward failed"
    driver.refresh()
    title2 = driver.find_element(By.XPATH, "//p[contains(text(), 'split testing')]")
    assert "split testing" in title2.text, "Refresh failed"
