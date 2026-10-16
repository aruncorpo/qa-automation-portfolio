from selenium.webdriver.common.by import By

def test_initialization(driver):
    driver.get('https://the-internet.herokuapp.com/windows')
    original_tab = driver.current_window_handle
    driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
    handles = driver.window_handles
    print(handles)
    new_tab = ""
    for handle in handles:
        if handle != original_tab:
            new_tab = handle
    driver.switch_to.window(new_tab)
    handles = driver.window_handles
    print(handles)
    driver.close()
    handles = driver.window_handles
    print(handles)
    driver.switch_to.window(original_tab)
    title = driver.find_element(By.XPATH,"//h3[text()='Opening a new window']")
    assert title.text == "Opening a new window","switch to original failed"
    #driver.quit() is handled by the fixture
