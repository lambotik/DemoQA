import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    start_time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    full_test_name = os.environ.get("PYTEST_CURRENT_TEST").split('::')
    test_name = full_test_name[-1]
    test_name = test_name.replace(' (setup)', '')
    print(f'\nStart Test: <{test_name}> {start_time}')
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path=r"C:\Users\lambo\PycharmProjects\resource\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    finish_time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
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
