import random

from selenium.webdriver.common.by import By


class FormsPageLocators:
    # Form
    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    INPUT_USER_EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    SELECT_GENDER = (By.XPATH, f'//label[@for="gender-radio-{random.randint(1,3)}"]')
    INPUT_MOBILE_NUBER = (By.XPATH, '//input[@id="userNumber"]')
    INPUT_DATE_OF_BIRTH = (By.XPATH, '//input[@id="dateOfBirthInput"]')
    INPUT_SUBJECTS = (By.XPATH, '//input[@id="subjectsInput"]')
    INPUT_HOBBIES = (By.XPATH, f'//label[@for="hobbies-checkbox-{random.randint(1,3)}"]')
    UPLOAD_PICTURE = (By.XPATH, '//input[@id="uploadPicture"]')
    INPUT_CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    SELECT_STATE = (By.XPATH, '//div[@id="state"]')
    INPUT_STATE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    STATE_TEXT = (By.XPATH, '//*[@id="state"]/div/div[1]/div[1]')
    SELECT_CITY = (By.XPATH, '//div[@id="city"]')
    INPUT_CITY = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    CITY_TEXT = (By.XPATH, '//*[@id="city"]/div/div[1]/div[1]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # Result Table
    TABLE_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')


