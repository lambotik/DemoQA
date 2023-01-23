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


class FramePageLocators:
    BIG_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    SMALL_FRAME = (By.XPATH, '//iframe[@id="frame2"]')
    TITLE_FRAME = (By.XPATH, '//h1[@id="sampleHeading"]')


class NestedFramePageLocators:
    PARENT_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogPageLocators:
    SMALL_MODAL = (By.XPATH, "//button[@id='showSmallModal']")
    SMALL_MODAL_TITLE = (By.XPATH, '//div[@id="example-modal-sizes-title-sm"]')
    SMALL_MODAL_TEXT = (By.XPATH, "//div[@class='modal-body']")
    CLOSE_SMALL_MODAL = (By.XPATH, "//button[@id='closeSmallModal']")
    LARGE_MODAL = (By.XPATH, "//button[@id='showLargeModal']")
    LARGE_MODAL_TITLE = (By.XPATH, '//div[@id="example-modal-sizes-title-lg"]')
    LARGE_MODAL_TEXT = (By.XPATH, "//div[@class='modal-body']")
    CLOSE_LARGE_MODAL = (By.XPATH, "//button[@id='closeLargeModal']")