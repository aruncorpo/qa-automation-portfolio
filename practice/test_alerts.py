from selenium.webdriver.common.by import By

def test_initialization(driver):
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    text = driver.find_element(By.XPATH,"//h3[text()='JavaScript Alerts']").text
    assert text == "JavaScript Alerts", "Page loading failed"

    driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", "Alert cant be reached"
    alert.accept()
    result = driver.find_element(By.XPATH,"//p[text()='You successfully clicked an alert']")
    assert result.text == "You successfully clicked an alert", "No changes on page"

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert2 = driver.switch_to.alert
    assert alert2.text == "I am a JS Confirm", "Alert cant be reached"
    alert2.accept()
    result = driver.find_element(By.XPATH, "//p[text()='You clicked: Ok']")
    assert result.text == "You clicked: Ok", "No changes on page"

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert2 = driver.switch_to.alert
    assert alert2.text == "I am a JS Confirm", "Alert cant be reached"
    alert2.dismiss()
    result = driver.find_element(By.XPATH, "//p[text()='You clicked: Cancel']")
    assert result.text == "You clicked: Cancel", "No changes on page"

    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert3 = driver.switch_to.alert
    assert alert3.text == "I am a JS prompt", "Alert cant be reached"
    alert3.send_keys("Buttercups")
    alert3.accept()
    result = driver.find_element(By.XPATH, "//p[text()='You entered: Buttercups']")
    assert result.text == "You entered: Buttercups", "No changes on page"