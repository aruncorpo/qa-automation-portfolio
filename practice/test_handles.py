from selenium.webdriver.common.by import By

def test_initialization(driver):
    driver.get('https://the-internet.herokuapp.com/windows')
    original_tab = driver.current_window_handle
    driver.find_element(By.LINK_TEXT,"Click Here").click()
    handles = driver.window_handles
    new_tab = ""
    for handle in handles:
        if handle != original_tab:
            new_tab = handle
    driver.switch_to.window(new_tab)

    text = driver.find_element(By.XPATH, "//h3[text()='New Window']")
    assert text.text == "New Window", "Window not open"

    driver.switch_to.window(original_tab)
    text = driver.find_element(By.XPATH, "//h3[text()='Opening a new window']")
    assert text.text == "Opening a new window", "Window not open"