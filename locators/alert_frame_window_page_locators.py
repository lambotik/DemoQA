from selenium.webdriver.common.by import By


class AlertFrameWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')
    NEW_WINDOW_MESSAGE_BUTTON = (By.XPATH, '//button[@id="messageWindowButton"]')
    SAMPLE_PAGE = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_MESSAGE = (By.XPATH, '/html/body/text()')
