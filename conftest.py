import datetime
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    start_time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    full_test_name = os.environ.get("PYTEST_CURRENT_TEST").split('::')
    test_name = full_test_name[-1]
    test_name = test_name.replace(' (setup)', '')
    print(f'\nStart Test: <{test_name}> {start_time}')
    driver = webdriver.Chrome(ChromeDriverManager().install())
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
