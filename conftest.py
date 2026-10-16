import pytest
import allure
from utils.screenshot_taker import take_screenshot
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.login_page import LoginPage
from tests.base_page import BasePage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--guest')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver,request):

    loginpage = LoginPage(driver)
    basepage = BasePage(driver)
    basepage.navigate('https://www.saucedemo.com/')
    username,password,expected = request.param
    loginpage.login(username, password)
    if loginpage.is_logged_in():
        yield driver
    else:
        print("login failed")

def pytest_runtest_makereport(call,item):

    if call.when != "call":
        return

    if call.excinfo is None:
        return

    if "driver" not in item.funcargs:
        return

    driver = item.funcargs.get("driver")

    date_time = datetime.now()
    item_name = item.name
    location = f"screenshots/"
    filename = (f"{date_time},{item_name}"
                .replace(":","-").replace("/","_")
                .replace("["," ").replace("]"," ")
                .replace("\\","_"))


    location_and_filename = f"{location} {filename}.png"

    take_screenshot(driver,location_and_filename)
    allure.attach.file(location_and_filename,
                       name=item_name,
                       attachment_type=allure.attachment_type.PNG,
                       )