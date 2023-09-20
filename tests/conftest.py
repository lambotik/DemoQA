from datetime import datetime
import os
import allure

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    try:
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    except UnexpectedAlertPresentException:
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    finish_time = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print(f'Test Finish: {finish_time}')
    driver.quit()


@pytest.fixture()
def set_up():
    print('Start Test')
    yield
    print('Finish Test')


@pytest.fixture(scope='module')
def set_group():
    print('Start System')
    yield
    print('Exit System')
