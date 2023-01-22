from selenium.webdriver.common.by import By


class AlertFrameWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')
    NEW_WINDOW_MESSAGE_BUTTON = (By.XPATH, '//button[@id="messageWindowButton"]')
    SAMPLE_PAGE = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_MESSAGE = (By.XPATH, '/html/body/text()')


class AlertsPageLocators:
    ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.XPATH, '//button[@id="timerAlertButton"]')
    CONFIRM_BUTTON_ALERT = (By.XPATH, '//button[@id="confirmButton"]')
    RESULT_CONFIRM_ALERT = (By.XPATH, '//span[@id="confirmResult"]')
    LOGIN_ALERT_BUTTON = (By.XPATH, '//button[@id="promtButton"]')
    PROMT_ALERT_RESULT = (By.XPATH, '//span[@id="promptResult"]')