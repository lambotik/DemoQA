from locators.alert_frame_window_page_locators import AlertFrameWindowsPageLocators
from pages.base_page import BasePage


class AlertFrameWindowsPage(BasePage):
    locators = AlertFrameWindowsPageLocators()

    def browser_window(self):
        pass


