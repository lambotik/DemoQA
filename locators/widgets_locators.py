from selenium.webdriver.common.by import By


class AccordianPageLocators:
    # Accordian
    FIRST_TAB = (By.XPATH, '//div[@id="section1Heading"]')
    FIRST_TAB_TEXT = (By.XPATH, '//div[@id="section1Content"]/p')
    SECOND_TAB = (By.XPATH, '//div[@id="section2Heading"]')
    SECOND_TAB_TEXT = (By.XPATH, '//div[@id="section2Content"]/p')
    THIRD_TAB = (By.XPATH, '//div[@id="section3Heading"]')
    THIRD_TAB_TEXT = (By.XPATH, '//div[@id="section3Content"]/p')


class AutoCompletePageLocators:
    # Auto complete
    INPUT_MULTI = (By.XPATH, '//input[@id="autoCompleteMultipleInput"]')
    LIST_MULTI_VALUE = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    CLOSE_MULTI_VALUE_ELEMENT = (
        By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    INPUT_SINGLE = (By.XPATH, '//input[@id="autoCompleteSingleInput"]')
    SINGLE_CONTAINER = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')
