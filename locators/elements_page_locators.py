from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Input Form
    INPUT_FULL_NAME = (By.XPATH, "//input[@id='userName']")
    INPUT_EMAIL = (By.XPATH, "//input[@id='userEmail']")
    INPUT_CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    INPUT_PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@id='submit']")
    JS_FULL_NAME = "#userName"

    # Created Form
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    TITLE_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECK_BOX_LIST = (By.XPATH, '//span[@class="rct-checkbox"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')
    # !!!В данном локаторе не указываем метод поиска, т.к. он указывается в функции
    TITLE_LIST_TEXT = './/ancestor::span[@class="rct-text"]'


class RadioButtonPageLocators:
    YES_BUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_BUTTON = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_TEXT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class WebTablePageLocators:
    ADD_BUTTON = (By.XPATH, '//button[@id="addNewRecordButton"]')
    INPUT_SEARCH = (By.XPATH, '//input[@id="searchBox"]')
    # Registration Form
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]')
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTAMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    CLOSE_FORM_REGISTRATION = (By.XPATH, '//button[@class="close"]')
    ALL_DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROW = (By.XPATH, '//div[@class="rt-noData"]')
    SELECT_NUMBER_ROWS = (By.XPATH, '//select[@aria-label="rows per page"]')
    # Table
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    # Update table
    EDIT_BUTTONS = (By.XPATH, '//span[@title="Edit"]')
    REGISTRATION_FORM_ALL_LINES = (By.CSS_SELECTOR, '.mr-sm-2.form-control')


class ButtonPageLocators:
    DOUBLE_CLICK = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME = (By.XPATH, '//button[. = "Click Me"]')
    DOUBLE_CLICK_MESSAGE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    RIGHT_MESSAGE = (By.XPATH, '//p[@id="rightClickMessage"]')
    CLICK_ME_MESSAGE = (By.XPATH, '//p[@id="dynamicClickMessage"]')

class LinksPageLocators:
    HOME_LINK = (By.XPATH, '//a[.="Home"]')
    BAD_REQUEST = (By.XPATH, '//a[@id="bad-request"]')



