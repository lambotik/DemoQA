from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    INPUT_FULL_NAME = (By.XPATH, "//input[@id='userName']")
    INPUT_EMAIL = (By.XPATH, "//input[@id='userEmail']")
    INPUT_CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    INPUT_PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@id='submit']")
    JS_FULL_NAME = "#userName"


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

    TITLE_LIST_TEXT = './/ancestor::span[@class="rct-text"]'


class RadioButtonPageLocators:
    YES_BUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_BUTTON = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_TEXT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    INPUT_SEARCH = (By.CSS_SELECTOR, 'input[id="searchBox"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTAMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    CLOSE_FORM_REGISTRATION = (By.XPATH, '//button[@class="close"]')
    ALL_DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROW = (By.XPATH, '//div[@class="rt-noData"]')
    SELECT_NUMBER_ROWS = (By.XPATH, '//select[@aria-label="rows per page"]')

    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')

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
    BAD_REQUEST_LINK = (By.XPATH, '//a[@id="bad-request"]')
    CREATED_LINK = (By.XPATH, '//a[@id="created"]')
    NO_CONTENT_LINK = (By.XPATH, '//a[@id="no-content"]')
    MOVED_LINK = (By.XPATH, '//a[@id="moved"]')
    UNAUTHORIZED_LINK = (By.XPATH, '//a[@id="unauthorized"]')
    FORBIDDEN_LINK = (By.XPATH, '//a[@id="forbidden"]')
    NOT_FOUND_LINK = (By.XPATH, '//a[@id="invalid-url"]')
    LINK_RESPONSE_CODE = (By.XPATH, '//*[@id="linkResponse"]/b[1]')


class UploadAndDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.XPATH, '//a[@id="downloadButton"]')
    UPLOAD_BUTTON = (By.XPATH, '//input[@id="uploadFile"]')
    RESULT_UPLOADED_BUTTON = (By.XPATH, '//p[@id="uploadedFilePath"]')

class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.XPATH, '//button[@id="colorChange"]')
    VISIBLE_AFTER_BUTTON = (By.XPATH, '//button[@id="visibleAfter"]')
    ENABLE_AFTER_BUTTON = (By.XPATH, '//button[@id="enableAfter"]')

