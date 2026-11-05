import pytest
import allure
import pathlib

from utils.screenshot_taker import take_screenshot
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from selenium.common import TimeoutException

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
    username, password, expected = request.param

    try:
        loginpage.login(username, password)
        if not loginpage.is_logged_in():
            pytest.fail(f"{username}logged_in_driver fixture creation failed")
    except (NoSuchElementException, TimeoutException):
        pytest.fail(f"{username}logged_in_driver fixture creation failed")

    yield driver

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

    location = pathlib.Path(__file__).resolve().parent / "screenshots"
    location.mkdir(parents=True, exist_ok=True)

    filename = (f"{date_time},{item_name}"
                .replace(":","-").replace("/","_")
                .replace("["," ").replace("]"," ")
                .replace("\\","_"))


    location_and_filename = str(location / f"{filename}.png")

    take_screenshot(driver,location_and_filename)
    allure.attach.file(location_and_filename,
                       name=item_name,
                       attachment_type=allure.attachment_type.PNG,
                       )