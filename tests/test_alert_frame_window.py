from pages.alerts_frame_windows_page import AlertFrameWindowsPage
from pages.base_page import BasePage


class TestAlertFrameWindowsPage:
    class TestAlertFrameWindows:
        def test_browser_window(self, driver):
            browser_window_page = AlertFrameWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()