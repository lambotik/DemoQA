from selenium.webdriver.common.by import By


class AccordianPageLocators:
    # Accordian
    FIRST_TAB = (By.XPATH, '//div[@id="section1Heading"]')
    FIRST_TAB_TEXT = (By.XPATH, '//div[@id="section1Content"]/p')
    SECOND_TAB = (By.XPATH, '//div[@id="section2Heading"]')
    SECOND_TAB_TEXT = (By.XPATH, '//div[@id="section2Content"]/p')
    THIRD_TAB = (By.XPATH, '//div[@id="section3Heading"]')
    THIRD_TAB_TEXT = (By.XPATH, '//div[@id="section3Content"]/p')
